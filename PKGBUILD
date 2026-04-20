# Maintainer: Alberto Garcia <berto@igalia.com>

pkgname='holo-nix-offload'
pkgver=0.3
pkgrel=1
pkgdesc="Holo Nix Offload"
arch=('any')
license=('LGPL2.1')
depends=('steamos-customizations-jupiter')
source=("nix.mount")
sha256sums=('5bd60a1a0911211b65edece545db83a5981a9c04c6e7b3f9d38fe6dbb2193a45')

package() {
    mkdir -m 0755 -p "$pkgdir"/nix
    mkdir -m 0755 -p "$pkgdir"/usr/lib/systemd/system/holo-offload.target.wants
    install -m 0644 -t "$pkgdir"/usr/lib/systemd/system nix.mount
    ln -s ../nix.mount "$pkgdir"/usr/lib/systemd/system/holo-offload.target.wants
}
