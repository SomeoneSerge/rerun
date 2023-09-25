{ pkgs ? import <nixpkgs> {
    overlays = [
      (builtins.getFlake github:SomeoneSerge/pkgs/master).overlay
    ];
  }
}:

with pkgs;

some-pkgs.callPackage ./package.nix { }
