pkgname=ibus-table-cangjie-lite
pkgver=1.8.8
pkgrel=1
_commit=d0f98492ffac6046d03ba052e585db99b7d27cc0   # Some Valve specific changes not yet upstreamed
pkgdesc="Some table-based input method of tables engines for IBus"
arch=('any')
url="https://github.com/mike-fabian/ibus-table-chinese"
license=('GPL3')
depends=('ibus-table')
makedepends=('cmake' 'python' 'noto-fonts-cjk' 'fontconfig' 'git')
source=("git+https://github.com/bjj/ibus-table-chinese.git#commit=$_commit"
  limit-to-cangjie.patch)
sha256sums=('SKIP'
  'cea245fec5c1775a2ade6717c1ac15965b247d1ac768835c94abea1c193dfa13')

prepare() {
  patch -d ibus-table-chinese -p1 -i ../limit-to-cangjie.patch
}

build() {
  cd ibus-table-chinese
  cmake . -DENABLE_TABLE_PREPROCESS=1 -DCMAKE_FEDORA_TMP_DIR=. -DDATA_DIR=/usr/share -DPRJ_DOC_DIR=/usr/share/doc/$pkgname -DCMAKE_INSTALL_PREFIX=/usr
  make
}

package() {
  cd ibus-table-chinese
  echo "pkgdir is $pkgdir"
  make DESTDIR="$pkgdir" install
}
