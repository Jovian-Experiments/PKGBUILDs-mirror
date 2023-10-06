# Maintainer: Vicki Pfau (vi@endrift.com)

pkgname=powerbuttond
_srctag=v2
pkgver=${_srctag##v}
pkgrel=1
arch=('x86_64')
url="https://gitlab.steamos.cloud/jupiter/powerbuttond"
pkgdesc="Power button daemon"
license=('BSD')
depends=('libevdev')
source=("git+ssh://git@gitlab.steamos.cloud/jupiter/powerbuttond.git#tag=$_srctag")
sha512sums=(SKIP)

build() {
	make -C "$srcdir/$pkgname"
}

package() {
	make -C "$srcdir/$pkgname" install DESTDIR="$pkgdir"
}
