# Maintainer: Jan Alexander Steffens (heftig) <heftig@archlinux.org>
# Contributor: Bartłomiej Piotrowski <bpiotrowski@archlinux.org>
# Contributor: Jan Alexander Steffens (heftig) <jan.steffens@gmail.com>

# TODO: Keep at stable versions starting with 1.16.0
# https://gitlab.archlinux.org/archlinux/packaging/packages/flatpak/-/issues/1

pkgbase=flatpak
pkgname=(
  flatpak
  flatpak-docs
)
pkgver=1.15.10
pkgrel=1.1
epoch=1
pkgdesc="Linux application sandboxing and distribution framework (formerly xdg-app)"
url="https://flatpak.org"
arch=(x86_64)
license=(LGPL-2.1-or-later)
depends=(
  appstream
  bash
  bubblewrap
  curl
  dbus
  dconf
  fuse3
  gcc-libs
  gdk-pixbuf2
  glib2
  glibc
  gpgme
  json-glib
  libarchive
  libmalcontent
  libseccomp
  libxau
  libxml2
  ostree
  polkit
  'python>=3.11'
  'python<3.12'
  python-gobject
  systemd
  systemd-libs
  wayland
  xdg-dbus-proxy
  xdg-utils
  zstd
)
makedepends=(
  docbook-xsl
  git
# Holo: Arch split glib2 devel files into their own package
# glib2-devel
  gobject-introspection
  gtk-doc
  meson
  python-packaging
  python-pyparsing
  wayland-protocols
  xmlto
)
checkdepends=(
  socat
  valgrind
)
source=(
  "git+https://github.com/flatpak/flatpak?signed#tag=$pkgver"
  https://dl.flathub.org/repo/flathub.flatpakrepo
  flatpak-bindir.sh
)
b2sums=('SKIP'
        'c094461a28dab284c1d32cf470f38118a6cbce27acce633b81945fb859daef9bdec1261490f344221b5cacf4437f53934cb51173f7ad2f1d2e05001139e75c54'
        '1c45caa65e2a1598f219977d5a81dcb8ea5d458880c43c40ba452b0c77cbbf41b36fa6911741f22c807d318e04e39e4fcc1455ed8d68faaba10162dae2570abc')
validpgpkeys=(
  DA98F25C0871C49A59EAFF2C4DE8FF2A63C7CC90 # Simon McVittie <smcv@collabora.com>
)

prepare() {
  cd flatpak
}

build() {
  local meson_options=(
    -D dbus_config_dir=/usr/share/dbus-1/system.d
    -D selinux_module=disabled
    -D system_bubblewrap=bwrap
    -D system_dbus_proxy=xdg-dbus-proxy
  )

  arch-meson flatpak build "${meson_options[@]}"
  meson compile -C build
}

check() {
  # Broken and gets stuck in our containers
  : || meson test -C build --print-errorlogs
}

_pick() {
  local p="$1" f d; shift
  for f; do
    d="$srcdir/$p/${f#$pkgdir/}"
    mkdir -p "$(dirname "$d")"
    mv "$f" "$d"
    rmdir -p --ignore-fail-on-non-empty "$(dirname "$f")"
  done
}

package_flatpak() {
  depends+=(
    libostree-1.so
    xdg-desktop-portal
  )
  provides=(libflatpak.so)

  meson install -C build --destdir "$pkgdir"

  install -Dt "$pkgdir/etc/profile.d" -m644 flatpak-bindir.sh
  install -Dt "$pkgdir/etc/flatpak/remotes.d" flathub.flatpakrepo

  _pick docs "$pkgdir"/usr/share/{doc,gtk-doc}
}

package_flatpak-docs() {
  pkgdesc+=" (documentation)"
  depends=()
  mv docs/* "$pkgdir"
}

# vim:set sw=2 sts=-1 et:
