# Maintainer: Vicki Pfau (vi@endrift.com)

pkgname=wakehook
_srctag=v2
pkgver=${_srctag##v}
pkgrel=2
arch=('x86_64')
url="https://gitlab.steamos.cloud/endrift/wakehook"
pkgdesc="Simple HDMI-CEC wakeup-on-resume daemon"
license=('BSD')
depends=('libcec' 'plasma-remotecontrollers' 'systemd')
source=("git+ssh://git@gitlab.steamos.cloud/endrift/wakehook.git#tag=$_srctag"
        '0001-Add-systemd-service.patch')
sha256sums=(SKIP
            cc1bc5503697769a128ca55ed90ef6ce865144aa650ebb7e31f16b5dae084b78)

prepare() {
	patch -d "$srcdir/$pkgname" -p1 < "$srcdir/0001-Add-systemd-service.patch"
}

build() {
	make -C "$srcdir/$pkgname"
}

package() {
	make -C "$srcdir/$pkgname" install DESTDIR="$pkgdir"
}
