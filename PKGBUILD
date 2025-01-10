pkgname=ibus-table-cangjie-lite
pkgver=1.8.8
pkgrel=2.3
_commit=cc4a17fde8904c6e60ded3558c551c90d9b72454   # Some Valve specific changes not yet upstreamed
pkgdesc="Some table-based input method of tables engines for IBus"
arch=('any')
url="https://github.com/mike-fabian/ibus-table-chinese"
license=('GPL3')
depends=('ibus-table')
makedepends=('cmake' 'python>=3.13' 'python<3.14' 'noto-fonts-cjk' 'fontconfig' 'git')
source=("git+https://github.com/bjj/ibus-table-chinese.git#commit=$_commit"
  limit-tables.patch)
sha256sums=('SKIP'
  '3c75b1b182019b3ee69ea934626a62eb0e0a018b0757f32e0c1912041b9073d5')

prepare() {
  patch -d ibus-table-chinese -p1 -i ../limit-tables.patch
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
