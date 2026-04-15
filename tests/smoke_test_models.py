"""Lightweight checks for local HDF5 model artifacts.

This is intentionally quick: it verifies the expected model files exist and
start with the HDF5 signature used by Keras `.h5` model files.
"""

from __future__ import annotations

from pathlib import Path


MODEL_PATHS = (
    Path("models/pretrained/U_net.h5"),
    Path("models/pretrained/deeplab_model.h5"),
    Path("models/pretrained/hybrid_model.h5"),
    Path("models/saved/U_net.h5"),
    Path("models/saved/deeplab_model.h5"),
    Path("models/saved/hybrid_model.h5"),
)

HDF5_SIGNATURE = b"\x89HDF\r\n\x1a\n"


def main() -> None:
    missing: list[Path] = []
    invalid: list[Path] = []

    for model_path in MODEL_PATHS:
        if not model_path.exists():
            missing.append(model_path)
            continue

        with model_path.open("rb") as model_file:
            signature = model_file.read(len(HDF5_SIGNATURE))

        if signature != HDF5_SIGNATURE:
            invalid.append(model_path)
            continue

        size_mb = model_path.stat().st_size / (1024 * 1024)
        print(f"ok: {model_path} ({size_mb:.1f} MB)")

    if missing or invalid:
        for model_path in missing:
            print(f"missing: {model_path}")
        for model_path in invalid:
            print(f"invalid hdf5 signature: {model_path}")
        raise SystemExit(1)

    print("model smoke test passed")


if __name__ == "__main__":
    main()
