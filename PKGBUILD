# Maintainer: Jan Alexander Steffens (heftig) <heftig@archlinux.org>
# Contributor: Bartłomiej Piotrowski <bpiotrowski@archlinux.org>
# Contributor: Patrick Griffis <tingping@tingping.se>

pkgname=xdg-desktop-portal-gtk
pkgver=1.15.1
pkgrel=1.1 # Holo: Drop the gtk-portal.conf that Arch adds
pkgdesc="A backend implementation for xdg-desktop-portal using GTK"
url="https://github.com/flatpak/xdg-desktop-portal-gtk"
arch=(x86_64)
license=(LGPL)
depends=(
  gtk3
  gsettings-desktop-schemas
  xdg-desktop-portal
)
makedepends=(
  git
  meson
  python
)
optdepends=("evince: Print preview")
provides=(xdg-desktop-portal-impl)
_commit=54003825481c2b48fd0c42355b484469dea12020  # tags/1.15.1^0
source=("git+https://github.com/flatpak/xdg-desktop-portal-gtk#commit=$_commit")
b2sums=('SKIP')

pkgver() {
  cd $pkgname
  git describe --tags | sed 's/[^-]*-g/r&/;s/-/+/g'
}

prepare() {
  cd $pkgname
}

build() {
  local meson_options=(
    -D wallpaper=disabled
  )
  arch-meson $pkgname build "${meson_options[@]}"
  meson compile -C build
}

check() {
  meson test -C build --print-errorlogs
}

package() {
  meson install -C build --destdir "$pkgdir"

  # Holo: we do not need the gtk-portal.conf that Arch adds
}

# vim:set sw=2 sts=-1 et:
