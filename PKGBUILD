# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor: Kerrick Staley <mail@kerrickstaley.com>

pkgname=pyzy
pkgver=1.1
_commit="d7747466562cb8b4bc2934708e29b7643c7bedbc"
pkgrel=1.1
pkgdesc='The Chinese PinYin and Bopomofo conversion library'
arch=('x86_64')
url='https://github.com/pyzy/pyzy'
license=('LGPL')
depends=('glib2' 'sqlite' 'util-linux')
makedepends=('git' 'doxygen' 'gnome-common' 'python')
source=("git+https://github.com/pyzy/pyzy.git#commit=$_commit"
        pyzy-python3.patch)
sha512sums=('SKIP'
            '901900d6b7f40bd9910bb7a200dcb53096169cc6501d0ab34faf25b3e279b8dd0f41702bb48c9554803d2089ab43f245ca7ba98137462572f7625fb7992ec618')

build() {
  cd $pkgname
  patch -p1 -i ../pyzy-python3.patch

  ./autogen.sh --prefix=/usr
  sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0/g' libtool
  make
}

package() {
  cd "$srcdir/$pkgname"

  make DESTDIR="$pkgdir" install
}
