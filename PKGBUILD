# Maintainer: Nícolas F. R. A. Prado <nfraprado@collabora.com>
pkgname=ec-log
pkgver=0.1
pkgrel=1.1
pkgdesc="Forward EC log to system log"
arch=('any')
license=('MIT')
depends=('systemd' 'util-linux')
source=("$pkgname.service")
sha256sums=('2abaafc8890e51262d30c89ecf3c2b4c9a7b4f0dcdce7de6dc1a7cdab48413a6')

package() {
        install -Dm644 -t "$pkgdir/usr/lib/systemd/system/" "$pkgname.service"
}
