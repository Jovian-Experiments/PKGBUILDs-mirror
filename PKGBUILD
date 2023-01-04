# Maintainer: David Runge <dvzrv@archlinux.org>
# Maintainer: Jan Alexander Steffens (heftig) <heftig@archlinux.org>

pkgbase=wireplumber
pkgname=(wireplumber wireplumber-docs)
_commit=0b5ff5ff7429785e428fd1e1fc4fcd728c9b5cc4  # tags/0.4.13-dv
pkgver=0.4.13.4.dv
pkgrel=1
pkgdesc="Session / policy manager implementation for PipeWire"
url="https://pipewire.pages.freedesktop.org/wireplumber/"
arch=(x86_64)
license=(MIT)
makedepends=(git meson doxygen graphviz 'pipewire>=0.3.43' systemd glib2 lua
             gobject-introspection python-sphinx python-sphinx_rtd_theme
             python-breathe python-lxml
             # In individual package dependencies below, but needs to be installed at build time for the check() step.
             pipewire-audio)
options=(debug)
source=("$pkgbase::git+https://gitlab.steamos.cloud/jupiter/wireplumber.git#commit=$_commit")
sha256sums=('SKIP')

pkgver() {
  cd $pkgbase
  git describe --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
  local meson_options=(
    -D system-lua=true
    -D elogind=disabled
  )

  arch-meson $pkgbase build "${meson_options[@]}"
  meson compile -C build
}

check() {
  meson test -C build --print-errorlogs
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

package_wireplumber() {
  depends=('pipewire>=0.3.43' pipewire-audio lua libpipewire-0.3.so libsystemd.so
           libg{lib,module,object,io}-2.0.so)
  optdepends=('wireplumber-docs: Documentation')
  provides=(pipewire-session-manager libwireplumber-0.4.so)
  conflicts=(pipewire-media-session)
  install=wireplumber.install

  meson install -C build --destdir "$pkgdir"

  _pick docs "$pkgdir"/usr/share/doc

  install -Dt "$pkgdir/usr/share/doc/$pkgname" -m644 $pkgbase/{NEWS,README}*
  install -Dt "$pkgdir/usr/share/licenses/$pkgname" -m644 $pkgbase/LICENSE
}

package_wireplumber-docs() {
  pkgdesc+=" - documentation"

  mv docs/* "$pkgdir"

  install -Dt "$pkgdir/usr/share/licenses/$pkgname" -m644 $pkgbase/LICENSE
}

# vim:set sw=2 et:
