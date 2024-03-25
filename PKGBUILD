pkgname=holo-rust-packaging-tools
pkgver=0.1.1
pkgrel=1
pkgdesc="Packaging tools for Rust in Holo"
arch=(any)
url="https://gitlab.steamos.cloud/holo/rust-packaging/"
license=(MIT)
depends=(python)
makedepends=(python
             python-build
             python-installer
             python-setuptools
             python-wheel)
source=(
  "$pkgname-$pkgver::git+ssh://git@gitlab.steamos.cloud/holo/rust-packaging.git#tag=v$pkgver"
)
sha256sums=(SKIP)

build() {
  cd $pkgname-$pkgver
  make build
}

package() {
  cd $pkgname-$pkgver
  DESTDIR="$pkgdir" make install
}
