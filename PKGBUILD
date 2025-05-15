# Maintainer: Vicki Pfau (vi@endrift.com)

pkgname=steamos-powerbuttond
_srctag=v3.1
pkgver=${_srctag##v}
pkgrel=2
arch=('x86_64')
url="https://gitlab.steamos.cloud/holo/powerbuttond"
pkgdesc="Power button daemon for SteamOS"
license=('BSD')
depends=('libevdev' 'udev' 'gamescope')
source=("steamos-powerbuttond::git+ssh://git@gitlab.steamos.cloud/holo/powerbuttond.git#tag=$_srctag")
replaces=('powerbuttond')
conflicts=('powerbuttond')
provides=('powerbuttond')
sha512sums=(SKIP)

build() {
	make -C "$srcdir/$pkgname"
}

package() {
	make -C "$srcdir/$pkgname" install DESTDIR="$pkgdir"
}
