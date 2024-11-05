# Maintainer: Alberto Garcia <berto@igalia.com>

pkgname='holo-nix-offload'
pkgver=0.2
pkgrel=1
pkgdesc="SteamOS Nix Offload"
arch=('any')
license=('LGPL2.1')
depends=('steamos-customizations-jupiter')
source=("nix.mount")
sha256sums=('a5ba0949e279f0472ce26f2c0044f2cba6ba53e48331e2414c1bfa84d80e3e0a')

package() {
    mkdir -m 0755 -p "$pkgdir"/nix
    mkdir -m 0755 -p "$pkgdir"/usr/lib/systemd/system/steamos-offload.target.wants
    install -m 0644 -t "$pkgdir"/usr/lib/systemd/system nix.mount
    ln -s ../nix.mount "$pkgdir"/usr/lib/systemd/system/steamos-offload.target.wants
}
