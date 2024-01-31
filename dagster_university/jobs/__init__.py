from dagster import AssetSelection, define_asset_job
from ..partitions import monthly_partitions, weekly_partitions

trips_by_week = AssetSelection.keys(["trips_by_week"])

trip_update_job = define_asset_job(
    name="trip_update_job",
    selection=AssetSelection.all() - trips_by_week,
    partitions_def=monthly_partitions,
)

weekly_update_job = define_asset_job(
    name="weekly_update_job",
    selection=trips_by_week,
    partitions_def=weekly_partitions,
)