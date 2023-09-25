{ pkgs ? import <nixpkgs> {
    overlays = [
      (builtins.getFlake github:SomeoneSerge/pkgs/master).overlay
    ];
  }
}:

with pkgs;
mkShell {
  inputsFrom = [
    (import ./default.nix { inherit pkgs; })
  ];
  packages = [
    cargo
  ];
}
