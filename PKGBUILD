# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor: Kerrick Staley <mail@kerrickstaley.com>

pkgname=pyzy
pkgver=1.1
pkgrel=2.6
pkgdesc='The Chinese PinYin and Bopomofo conversion library'
arch=('x86_64')
license=('LGPL')
depends=('glib2' 'sqlite' 'util-linux')
makedepends=('doxygen' 'gnome-common' 'python>=3.14' 'python<3.15')
_commit=5ac51d833777a881e80f0b23d704345cf0feb0d0
source=(
  "git+https://github.com/openSUSE/pyzy#commit=${_commit}"
)
sha512sums=('8775834dbe93c92cbc8b3a021df2e25624894d8ee159a22f0a8ee3b07c640dfc564eb37a67f22e3e6ff6301d236646abb8afb68dfec248bda010bc67f92f0d35')

build() {
  cd ${pkgname}
  ./autogen.sh --prefix=/usr
  sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0/g' libtool
  make
}

package() {
  cd ${pkgname}
  make DESTDIR="$pkgdir" install
}
