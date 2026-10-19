# Maintainer: Nícolas F. R. A. Prado <nfraprado@collabora.com>
pkgname=jupiter-hibernate-disable
pkgver=0.1
pkgrel=1
pkgdesc="Disable hibernate for Jupiter/Galileo"
arch=('any')
license=('MIT')
depends=('systemd' 'dmidecode')
source=("$pkgname.service"
	"$pkgname.sh")
sha256sums=('6e87c58e3b91e640451c5ca5e012bcf972c52e1624c479e2ac51fb914ee4f91e'
            'c2ab7606a0ad50452af017f248c1f0aa4c39e680b5452ca2fcebbb9faf5c9019')

package() {
        install -Dm644 -t "$pkgdir/usr/lib/systemd/system/" "$pkgname.service"
        install -Dm755 -t "$pkgdir/usr/lib/holo/" "$pkgname.sh"
}
