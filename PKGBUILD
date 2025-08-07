pkgname=ibus-table-cangjie-lite
pkgver=1.8.8
pkgrel=2.4
_commit=cc4a17fde8904c6e60ded3558c551c90d9b72454   # Some Valve specific changes not yet upstreamed
pkgdesc="Some table-based input method of tables engines for IBus"
arch=('any')
url="https://github.com/mike-fabian/ibus-table-chinese"
license=('GPL3')
depends=('ibus-table')
makedepends=('cmake' 'python>=3.13' 'python<3.14' 'noto-fonts-cjk' 'fontconfig' 'git')
source=("git+https://github.com/bjj/ibus-table-chinese.git#commit=$_commit"
  limit-tables.patch

  # Holo: Import upstream fix for newer cmake
  347071955719eb10f87f1ac4aa37003f74ed657e.patch
  )
sha256sums=('22aacc2d16b9c76f267bc38aad8504043e38b2aaa5a2ec4b770bd4338407a1fd'
            '3c75b1b182019b3ee69ea934626a62eb0e0a018b0757f32e0c1912041b9073d5'
            '2a67e000fe696a5d80b79467c67faa55e8eb6159848cbb2295c0fbe01777e628')

prepare() {
  patch -d ibus-table-chinese -p1 -i ../limit-tables.patch
  patch -d ibus-table-chinese -p1 -i ../347071955719eb10f87f1ac4aa37003f74ed657e.patch
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
