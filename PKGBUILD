# Maintainer: Johannes Löthberg <johannes@kyriasis.com>
# Maintainer (Holo): Alberto Garcia <berto@igalia.com>
# Maintainer: Daniel M. Capella <polyzen@archlinux.org>

pkgname=pacman-contrib
pkgver=1.10.4
pkgrel=1.1
pkgdesc='Contributed scripts and tools for pacman systems'
arch=('x86_64')
url=https://gitlab.archlinux.org/pacman/pacman-contrib
license=('GPL')
depends=('fakeroot' 'pacman' 'perl')
makedepends=('asciidoc' 'git')
optdepends=(
  'diffutils: for pacdiff'
  'findutils: for pacdiff --find'
  'mlocate: for pacdiff --locate'
  'sudo: privilege elevation for several scripts'
  'vim: default merge program for pacdiff'
)
source=("git+$url.git#tag=v$pkgver"
        # Holo: Get the pacman db path from the config. Needed for supermin / virt-sparsify
        # https://gitlab.steamos.cloud/jupiter/tasks/-/issues/836
        # https://gitlab.archlinux.org/pacman/pacman-contrib/-/issues/30
        "pacman-db.patch")
b2sums=('SKIP'
        'c33489e28df16738f52a78a290594688756daf4c2ae7ac58064d877a5d2345005c60680cdb5c7b814d6b1e2fe4f46bf79393118e3ad6f55d712de01c6dad3a9b')
validpgpkeys=('04DC3FB1445FECA813C27EFAEA4F7B321A906AD9') # Daniel M. Capella <polyzen@archlinux.org>
#             '5134EF9EAF65F95B6BB1608E50FB9B273A9D0BB5')  # Johannes Löthberg <johannes@kyriasis.com>

prepare() {
  cd $pkgname
  patch -p1 < "${srcdir}/pacman-db.patch"
  ./autogen.sh
}

build() {
  cd $pkgname
  ./configure \
    --prefix=/usr \
    --sysconfdir=/etc \
    --localstatedir=/var
  make
}

check() {
  cd $pkgname
  make check
}

package() {
  cd $pkgname
  make DESTDIR="$pkgdir" install
}

# vim:set ts=2 sw=2 et:
