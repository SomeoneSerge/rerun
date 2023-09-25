{ lib
, arrow-cpp
, binaryen
, cargo
, cargo-binutils
, catch2_3
, cmake
, darwin
, fetchFromGitHub
, libxkbcommon
, lld
, loguru
, pkg-config
, protobuf
, rustc-wasm32
, rustPackages_1_72
, rustPackages ? rustPackages_1_72
, rustPlatform ? rustPackages.rustPlatform
, stdenv
, vulkan-loader
, wayland
}:

rustPlatform.buildRustPackage rec {
  pname = "rerun";
  version = "unstable-2023-09-24";

  src = lib.cleanSource ./.;

  cargoLock = {
    lockFile = ./Cargo.lock;
    outputHashes = {
      "ecolor-0.22.0" = "sha256-RJRmbRhpyEbu2mBWEV+8R5+v8+UF1D8ooZ0CpYfgeV4=";
      "egui_commonmark-0.7.4" = "sha256-jD4xeDjmoD5BoCyXyIJh2p98qz95qk2L904tnfNSx0c=";
      "egui_tiles-0.2.0" = "sha256-DdaXhi0oQwMPO+hbHesJ+MzNlZA9pTnjMNyx3a63iuM=";
    };
  };

  buildFeatures = [
    "analytics"
    "demo"
    "glam"
    "image"
    "sdk"
    "server"
  ];

  cargoBuildFlags = [
    "-p"
    "re_viewer"
    "-p"
    "rerun"
  ];

  cargoTestFlags = cargoBuildFlags;

  nativeBuildInputs = [
    binaryen
    cargo-binutils # rust-lld
    cmake
    pkg-config
    protobuf
    # rustc-wasm32
    # rustc-wasm32.llvmPackages.lld
  ];

  buildInputs = [
    arrow-cpp
    catch2_3
    libxkbcommon
    loguru
    vulkan-loader
  ] ++ lib.optionals stdenv.isDarwin [
    darwin.apple_sdk.frameworks.AppKit
    darwin.apple_sdk.frameworks.CoreFoundation
    darwin.apple_sdk.frameworks.CoreGraphics
    darwin.apple_sdk.frameworks.CoreServices
    darwin.apple_sdk.frameworks.Foundation
    darwin.apple_sdk.frameworks.IOKit
    darwin.apple_sdk.frameworks.Metal
    darwin.apple_sdk.frameworks.QuartzCore
    darwin.apple_sdk.frameworks.Security
  ] ++ lib.optionals stdenv.isLinux [
    wayland
  ];

  meta = with lib; {
    description = "Log images, point clouds, etc, and visualize them effortlessly. Built in Rust using egui";
    homepage = "https://github.com/rerun-io/rerun";
    changelog = "https://github.com/rerun-io/rerun/blob/${src.rev}/CHANGELOG.md";
    license = with licenses; [ asl20 mit ];
    maintainers = with maintainers; [ ];
    mainProgram = "rerun";
    platforms = platforms.all;
  };
}
