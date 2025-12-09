import csv
import json
import os
import sys
import asyncio
import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.database import async_session, engine, Base
from app.assets.models import Asset
from app.signals.models import Signal
from app.measurements.models import Measurement

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

DATA_DIR = os.path.join(BASE_DIR, "app/data")
ASSETS_JSON = os.path.join(DATA_DIR, "assets.json")
SIGNALS_JSON = os.path.join(DATA_DIR, "signal.json")
MEASUREMENTS_CSV = os.path.join(DATA_DIR, "measurements.csv")


async def seed():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with async_session() as session:
        # Assets
        try:
            with open(ASSETS_JSON, "r") as f:
                assets_data = json.load(f)

            for a in assets_data:
                asset = Asset(
                    asset_id=a.get("AssetID"),
                    latitude=float(a.get("Latitude")),
                    longitude=float(a.get("Longitude")),
                    description=a.get("descri")
                )

                session.add(asset)

            await session.commit()
            print("Assets seeded")
        except FileNotFoundError:
            print(f"File {ASSETS_JSON} not found")
        except Exception as e:
            print(e)

        # ---------------- SIGNALS ----------------
        try:
            with open(SIGNALS_JSON, "r") as f:
                signals_data = json.load(f)

            for s in signals_data:

                session.add(Signal(
                    signal_gid=s.get("SignalGId"),
                    signal_id=int(s.get("SignalId")),
                    signal_name=s.get("SignalName"),
                    unit=s.get("Unit"),
                    asset_id=int(s.get("AssetId")),
                ))

            await session.commit()
            print("Signals seeded")
        except FileNotFoundError:
            print(f"File {SIGNALS_JSON} not found")
        except Exception as e:
            print(e)

        try:
            with open(MEASUREMENTS_CSV, newline="", encoding="utf-8-sig") as f:
                # pipe como separador
                reader = csv.DictReader(f, delimiter='|')
                for m in reader:
                    session.add(Measurement(
                        signal_id=int(m.get("SignalId")),
                        timestamp=datetime.datetime.strptime(
                            m.get("Ts"), "%Y-%m-%d %H:%M:%S.%f"),
                        value=float(
                            m.get("MeasurementValue").replace(",", ".")),
                        unit="kV"
                    ))

                await session.commit()
                print("Measurements seeded")
        except FileNotFoundError:
            print(f"File {MEASUREMENTS_CSV} not found")
        except Exception as e:
            print(e)

    print("DB seeding completed.")


if __name__ == "__main__":
    asyncio.run(seed())
