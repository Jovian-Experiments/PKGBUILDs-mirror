# Maintainer: Vicki Pfau (vi@endrift.com)

pkgname=wakehook
_srctag=v2
pkgver=${_srctag##v}
pkgrel=1
arch=('x86_64')
url="https://gitlab.steamos.cloud/endrift/wakehook"
pkgdesc="Simple HDMI-CEC wakeup-on-resume daemon"
license=('BSD')
depends=('libcec' 'plasma-remotecontrollers' 'systemd')
source=("git+ssh://git@gitlab.steamos.cloud/endrift/wakehook.git#tag=$_srctag")
sha512sums=(SKIP)

build() {
	make -C "$srcdir/$pkgname"
}

package() {
	make -C "$srcdir/$pkgname" install DESTDIR="$pkgdir"
}
