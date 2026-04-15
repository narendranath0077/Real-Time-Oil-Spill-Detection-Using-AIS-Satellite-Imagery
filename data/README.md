# Data

This folder keeps AIS data and oil-spill segmentation image data separated from code.

```text
data/
|-- ais/
|   |-- raw/          # Large original AIS CSV exports, ignored by Git
|   `-- processed/    # Small filtered CSV outputs used for analysis
`-- oil-spill-dataset/
    |-- train/
    `-- test/
```

The raw AIS exports and image dataset are kept locally because they are large. Small processed CSV files can be committed when they are useful for reproducing project results.
