# Maintainer: Jan Alexander Steffens (heftig) <heftig@archlinux.org>
# Contributor: Bartłomiej Piotrowski <bpiotrowski@archlinux.org>
# Contributor: Patrick Griffis <tingping@tingping.se>

pkgname=xdg-desktop-portal
pkgver=1.12.1
pkgrel=1.1
pkgdesc="Desktop integration portals for sandboxed apps"
url="https://github.com/flatpak/xdg-desktop-portal"
arch=(x86_64)
license=(LGPL)
depends=(glib2 pipewire fuse2 geoclue2)
makedepends=(python xmlto docbook-xsl git flatpak libportal)
checkdepends=(epiphany gedit gvfs)
_commit=6241c5e8bfb60502ac3c7bc3babede22d35f3b1c  # tags/1.12.1^0
source=("git+https://github.com/flatpak/xdg-desktop-portal#commit=$_commit"
        stop-portal-on-session-exit.patch)
sha256sums=('SKIP'
            e466fc4722d4169451064f4a147f9e6e827105938a844c10f78f8cb15cb7ec98)

pkgver() {
  cd $pkgname
  git describe --tags | sed 's/[^-]*-g/r&/;s/-/+/g'
}

prepare() {
  cd $pkgname
  patch -p1 -i "${srcdir}"/stop-portal-on-session-exit.patch
  NOCONFIGURE=1 ./autogen.sh
}

build() {
  cd $pkgname
  ./configure --prefix=/usr --libexecdir=/usr/lib
  make 
}

check() {
  cd $pkgname
  make check
}

package() {
  depends+=(xdg-desktop-portal-impl)

  cd $pkgname
  make DESTDIR="$pkgdir" install
}
