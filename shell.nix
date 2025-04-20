{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  name = "adb-aapt-env";

  buildInputs = [
    pkgs.android-tools  # Provides adb
    pkgs.aapt  # Provides aapt
  ];

  shellHook = ''
    export PATH=$PATH:${pkgs.aapt}/bin
    echo "ADB and AAPT environment ready."
  '';
}

