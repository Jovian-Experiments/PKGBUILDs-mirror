# Maintainer: Joshua Ashton <joshua@froggi.es>
# Contributor: Sébastien Luttringer <seblu@archlinux.org>
# Contributor: Tom Gundersen <teg@jklm.no>
# Contributor: Joel Teichroeb <joel@teichroeb.net>

pkgbase=wayland
pkgname=(wayland wayland-docs)
pkgver=1.23.0
pkgrel=1
pkgdesc='A computer display server protocol'
arch=('x86_64')
url='https://wayland.freedesktop.org/'
license=('MIT')
depends=('glibc' 'libffi' 'expat' 'libxml2' 'default-cursors')
makedepends=('meson' 'libxslt' 'doxygen' 'xmlto' 'graphviz' 'docbook-xsl')
validpgpkeys=('C7223EBE4EF66513B892598911A30156E0E67611'  # Bryce Harrington
              'C0066D7DB8E9AC6844D728715E54498E697F11D7'  # Derek Foreman
              '34FF9526CFEF0E97A340E2E40FDE7BE0E88F5E48') # emersion <contact@emersion.fr>
source=("https://gitlab.freedesktop.org/wayland/wayland/-/releases/$pkgver/downloads/wayland-$pkgver.tar.xz"{,.sig})
sha256sums=('05b3e1574d3e67626b5974f862f36b5b427c7ceeb965cb36a4e6c2d342e45ab2'
            'SKIP')

build() {
  arch-meson $pkgbase-$pkgver build
  meson compile -C build
}

check() {
  meson test -C build --print-errorlogs
}

package_wayland() {
  provides=(libwayland-{client,cursor,egl,server}.so)

  meson install -C build --destdir "$pkgdir"
  mkdir -p docs/share
  mv "$pkgdir"/usr/share/{doc,man} docs/share
  install -Dm 644 $pkgbase-$pkgver/COPYING "$pkgdir/usr/share/licenses/$pkgname/COPYING"
}

package_wayland-docs() {
  pkgdesc+=" (documentation)"
  depends=()

  mv docs "$pkgdir/usr"
  install -Dm 644 $pkgbase-$pkgver/COPYING "$pkgdir/usr/share/licenses/$pkgname/COPYING"
}

# vim:set sw=2 sts=-1 et:
