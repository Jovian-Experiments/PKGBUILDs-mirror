# Maintainer: Your Name <youremail@domain.com>
_pkgname=crcmod
pkgname=python-crcmod
pkgver=1.7
pkgrel=1
pkgdesc="Python module for generating objects that compute the Cyclic Redundancy Check (CRC)."
arch=('x86_64')
url="https://pypi.python.org/pypi/crcmod/"
license=('MIT')
depends=('python')
makedepends=('python-setuptools')
options=(!emptydirs)
source=("https://pypi.python.org/packages/source/c/$_pkgname/$_pkgname-${pkgver}.tar.gz")
sha256sums=('dc7051a0db5f2bd48665a990d3ec1cc305a466a77358ca4492826f41f283601e')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  python setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  python setup.py install --root="$pkgdir/" --optimize=1 --skip-build
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.md"
}

# vim:set ts=2 sw=2 et:
