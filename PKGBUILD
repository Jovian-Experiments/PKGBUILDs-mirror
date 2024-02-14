# Maintainer: Joshua Ashton <joshua@froggi.es>

pkgname=galileo-mura
_srctag=v0.4
pkgver=${_srctag//-/.}
pkgrel=1
pkgdesc="Utilities for setting and reading mura correction on Galileo"
arch=(x86_64)
url="https://gitlab.steamos.cloud/jupiter/galileo-mura-extractor"
license=('MIT')
depends=('tar' 'sed')
makedepends=(meson ninja)
source=("git+ssh://git@gitlab.steamos.cloud/jupiter/galileo-mura-extractor.git#tag=$_srctag")
sha256sums=('SKIP')

install=galileo-mura.install

prepare() {
	cd "galileo-mura-extractor"
}

build() {
	cd "galileo-mura-extractor"

	rm -rf build
	mkdir build
	cd build
	arch-meson --buildtype release --prefix /usr ..
	ninja
}

package() {
	cd "galileo-mura-extractor/build"

	DESTDIR="$pkgdir" meson install --skip-subprojects
}
