# Maintainer: Alberto Garcia <berto@igalia.com>

pkgname='holo-nix-offload'
pkgver=0.1
pkgrel=1
pkgdesc="SteamOS Nix Offload"
arch=('any')
license=('LGPL2.1')
depends=('steamos-customizations-jupiter')
source=("nix.mount")
sha256sums=('8aee780339355957845cfb9bac775ca7c15afb23e4f5fdce95c7d1b12162060e')

package() {
    mkdir -m 0755 -p "$pkgdir"/nix
    mkdir -m 0755 -p "$pkgdir"/usr/lib/systemd/system/steamos-offload.target.wants
    install -m 0644 -t "$pkgdir"/usr/lib/systemd/system nix.mount
    ln -s ../nix.mount "$pkgdir"/usr/lib/systemd/system/steamos-offload.target.wants
}
