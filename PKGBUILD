# Maintainer: Jan Alexander Steffens (heftig) <heftig@archlinux.org>
# Contributor: Bartłomiej Piotrowski <bpiotrowski@archlinux.org>
# Contributor: Patrick Griffis <tingping@tingping.se>

pkgname=xdg-desktop-portal
pkgver=1.16.0
pkgrel=1.1
pkgdesc="Desktop integration portals for sandboxed apps"
url="https://github.com/flatpak/xdg-desktop-portal"
arch=(x86_64)
license=(LGPL)
depends=(glib2 pipewire fuse3 geoclue rtkit systemd)
makedepends=(meson xmlto docbook-xsl git flatpak libportal)
_commit=88af6c8ca4106fcf70925355350a669848e9fd5a  # tags/1.16.0^0
source=("git+https://github.com/flatpak/xdg-desktop-portal#commit=$_commit"
        portal-configuration-file.patch)
sha256sums=('SKIP'
            '321a19c3236fc5f138808e2a9dd757c00b9a7cf381d02c1f1896a006cffa30f4')

pkgver() {
  cd $pkgname
  git describe --tags | sed 's/[^-]*-g/r&/;s/-/+/g'
}

prepare() {
  cd $pkgname

  # Add support for portals configuration; remove when upgrading to 1.18
  # See: https://github.com/flatpak/xdg-desktop-portal/issues/906
  git apply -3 "$srcdir/portal-configuration-file.patch"
}

build() {
  arch-meson $pkgname build
  meson compile -C build
}

check() {
  meson test -C build --print-errorlogs
}

package() {
  depends+=(xdg-desktop-portal-impl)

  meson install -C build --destdir "$pkgdir"
}

# vim:set sw=2 sts=-1 et:
