# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor: Kerrick Staley <mail@kerrickstaley.com>

pkgname=pyzy
pkgver=1.1
pkgrel=2.2
pkgdesc='The Chinese PinYin and Bopomofo conversion library'
arch=('x86_64')
license=('LGPL')
depends=('glib2' 'sqlite' 'util-linux')
makedepends=('doxygen' 'gnome-common' 'python')
_commit=ec719d053bd491ec64fe68fe0d1699ca6039ad80
source=(
  "git+https://github.com/openSUSE/pyzy#commit=${_commit}"
  'fix_preedit.patch'
)
sha512sums=(
  'SKIP'
  '8580c7b1a4b421294e2430c392709f4e57fb534ff6e9b6373c4975301c2d15057eaecdc9fd418418fca80f9a6465465ae5b7e7fdf8017f9a1eee7255777af54f'
)

prepare() {
  cd ${pkgname}
  # https://github.com/openSUSE/pyzy/commit/0949bb294c29a2790554884093d82ff40ed40759
  # this looks like a bug that snuck through - see comments
  patch -p1 -R -i ../fix_preedit.patch
}

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
