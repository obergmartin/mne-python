import mne
import pandas as pd
from mne.datasets.testing import data_path, requires_testing_data

testing_path = data_path(download=True)

# raw = mne.io.read_raw(
# "../../../currentStudies/kid-wlt/netstation/kwlt_sub-104_ses-1_20251122_102320.mff/")
egi_fname_mff = testing_path / "EGI" / "test_egi_pns_bug.mff"
egi_fname_mff = "../../../currentStudies/kid-wlt/netstation/kwlt_sub-104_ses-1_20251122_102320.mff/"
egi_fname_mff = testing_path / "EGI" / "test_egi.mff"
raw = mne.io.read_raw_egi(
    egi_fname_mff, include=None, preload=False, verbose="warning"
)
for a in raw.annotations[:15]:
    print(a)

df = pd.DataFrame(raw.annotations.extras)
print(df)
