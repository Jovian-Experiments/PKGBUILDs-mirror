# Maintainer: Johannes Löthberg <johannes@kyriasis.com>
# Maintainer (Holo): Alberto Garcia <berto@igalia.com>
# Maintainer: Daniel M. Capella <polyzen@archlinux.org>

pkgname=pacman-contrib
pkgver=1.7.1
pkgrel=1.1
pkgdesc='Contributed scripts and tools for pacman systems'
arch=('x86_64')
url=https://gitlab.archlinux.org/pacman/pacman-contrib
license=('GPL')
depends=('fakeroot' 'pacman' 'perl')
makedepends=('asciidoc')
optdepends=('diffutils: for pacdiff'
            'findutils: for pacdiff --find'
            'mlocate: for pacdiff --locate'
            'sudo: privilege elevation for several scripts'
            'vim: default merge program for pacdiff')
source=("$url/-/archive/v$pkgver/$pkgname-v$pkgver.tar.gz"
        # Holo: Get the pacman db path from the config. Needed for supermin / virt-sparsify
        # https://gitlab.steamos.cloud/jupiter/tasks/-/issues/836
        # https://gitlab.archlinux.org/pacman/pacman-contrib/-/issues/30
        "pacman-db.patch")
b2sums=('ab708c285cb19320a01aadfdce2cea7152278411d59f2c0f353e30061f415bd1feb926f18d8ef1f8ab43950ed9c4dd1e91deaad9562564a8cf01655e390c5d9d'
        'd1c2a94a5b76d8798fd66ca534dd9deb9179d605ff88543d2b798b4b34f527111a31e1feffaa106d29cda350f1dd241e438cf01a7195c15abdf861254dd23446')
#validpgpkeys=('5134EF9EAF65F95B6BB1608E50FB9B273A9D0BB5'  # Johannes Löthberg <johannes@kyriasis.com>
#              '04DC3FB1445FECA813C27EFAEA4F7B321A906AD9') # Daniel M. Capella <polyzen@archlinux.org>

prepare() {
  cd $pkgname-v$pkgver
  patch -p1 < "${srcdir}/pacman-db.patch"
  ./autogen.sh
}

build() {
  cd $pkgname-v$pkgver
  ./configure \
    --prefix=/usr \
    --sysconfdir=/etc \
    --localstatedir=/var
  make
}

check() {
  cd $pkgname-v$pkgver
  make check
}

package() {
  cd $pkgname-v$pkgver
  make DESTDIR="$pkgdir" install
}

# vim:set ts=2 sw=2 et:
