{
  description = "Flake to manage DedSec grub themes from Vandal";

  inputs = {
    nixpkgs.url = github:NixOS/nixpkgs/nixpkgs-unstable;
  };

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs { inherit system; };
    in
    with nixpkgs.lib;
    {
      nixosModule = { config, ... }:
        let
          cfg = config.boot.loader.grub.dedsec-theme;

          dedsec-grub-theme = pkgs.stdenv.mkDerivation {
            name = "decsec-grub-theme";
            src = ./.;
            installPhase = ''
              mkdir -p $out/grub/theme/
              
              cp assets/backgrounds/${cfg.style}-${cfg.resolution}.png $out/grub/theme/background.png
              cp -r assets/icons-${cfg.resolution}/${cfg.icon}/ $out/grub/theme/icons/
              cp -r assets/fonts/${cfg.resolution}/* $out/grub/theme/
              cp -r base/${cfg.resolution}/* $out/grub/theme
            '';
          };
        in
        {
          options = {
            boot.loader.grub.dedsec-theme = {
              enable = mkOption {
                type = types.bool;
                default = false;
                example = true;
                description = ''
                  Enable DedSec grub theme from Vandal
                '';
              };
              style = mkOption {
                type = types.enum [
                  "brainwash"
                  "compact"
                  "comments"
                  "firewall"
                  "fuckery"
                  "hackerden"
                  "legion"
                  "lovetrap"
                  "mashup"
                  "reaper"
                  "redskull"
                  "stalker"
                  "spam"
                  "spyware"
                  "strike"
                  "sitedown"
                  "trolls"
                  "tremor"
                  "unite"
                  "wannacry"
                  "wrench"
                ];
                example = "hackerden";
                description = ''
                  The theme to use for grub
                '';
              };
              icon = mkOption {
                type = types.enum [ "color" "white" ];
                default = "color";
                example = "color";
              };
              resolution = mkOption {
                type = types.enum [ "1080p" "1440p" ];
                default = "1080p";
                example = "1080p";
              };

            };
          };

          config = mkIf cfg.enable (mkMerge [{
            environment.systemPackages = [ dedsec-grub-theme ];
            boot.loader.grub = {
              theme = "${dedsec-grub-theme}/grub/theme";
            };
          }]);
        };
    };
}
