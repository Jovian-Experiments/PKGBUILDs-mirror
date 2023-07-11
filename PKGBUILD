# Maintainer: Vicki Pfau <vi@endrift.com>

pkgname=ds-inhibit
_srctag=0.1.1
pkgver=${_srctag}
pkgrel=1
pkgdesc="DualShock 4/DualSense mouse inhibitor"
url="https://gitlab.steamos.cloud/endrift/ds-inhibit"
arch=('any')
license=('BSD')
source=("git+ssh://git@gitlab.steamos.cloud/endrift/ds-inhibit#tag=v${_srctag}")
sha256sums=('SKIP')
depends=('udev' 'python' 'python-pyinotify')
makedepends=('git' 'openssh')

package() {
	cd "$pkgname"
	make install DESTDIR="$pkgdir"
	install -m644 -Dt "${pkgdir}/usr/share/licenses/${pkgname}" LICENSE
}
