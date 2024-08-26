# Maintainer: David Runge <dvzrv@archlinux.org>
# Maintainer: Jan Alexander Steffens (heftig) <heftig@archlinux.org>
# Maintainer (Holo): Ludovico de Nittis <denittis@collabora.com>

pkgbase=wireplumber
pkgname=(
  wireplumber
  libwireplumber
)
_tag=0.5.5
pkgver=${_tag//-/.}
pkgrel=1.1
pkgdesc="Session / policy manager implementation for PipeWire"
url="https://pipewire.pages.freedesktop.org/wireplumber/"
arch=(x86_64)
license=(MIT)
makedepends=(
  doxygen
  gcc-libs
  git
  glib2
  glibc
  gobject-introspection
  graphviz
  'libpipewire>=1:1.0.3'
  lua
  meson
  'pipewire>=1:1.0.3'
  python-breathe
  python-lxml
  python-sphinx
  python-sphinx_rtd_theme
  systemd
  systemd-libs
)
checkdepends=('pipewire-audio>=1:1.0.3')
options=(debug)
source=(
  "git+https://gitlab.freedesktop.org/pipewire/$pkgbase.git#tag=$_tag"

  # from https://gitlab.freedesktop.org/pipewire/wireplumber/-/merge_requests/655
  "0003-rescan-Merge-filters-metadata-changed-hook-with-resc.patch" # holo-team/tasks/-/issues/881 ETA 0.5.6
  "0004-rescan-Stop-rescan-for-2s-if-BT-node-is-removed.patch"      # holo-team/tasks/-/issues/881 ETA 0.5.6
)
b2sums=(
  'SKIP'
  '5034eb85057dc4c6c1c139d7ffdcb794db5d560f92457905ea8f4a0bada2c141130cd864889588652b0247032f2ed06c522e4d89baf93f55d557c1d884d4006b'
  '799d20f383047e441a8946cce8e07c053b2d5e136a8bbf8518b328ce6b1063f0455d083e3917d9f41e3edbd28210840b26c21b5e7ca92236984428437a228267'
)

prepare() {
  cd $pkgbase

  # Holo: apply downstream patches
  local src
  for src in "${source[@]}"; do
    [[ $src = *.patch ]] || continue
    src="${src##*/}"
    echo "Applying patch $src..."
    patch -Np1 < "../$src"
  done
}

build() {
  local meson_options=(
    -D elogind=disabled
    -D system-lua=true
    -D doc=disabled # HOLO: Fails due to some locale gubbins -- disable.
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

_ver=${pkgver:0:3}

package_wireplumber() {
  depends=(
    "libwireplumber=$pkgver-$pkgrel"
    gcc-libs
    glibc
    libg{lib,object,io}-2.0.so
    libpipewire
    libpipewire-0.3.so
    libsystemd.so
    lua
    'pipewire>=1:1.0.3'
    systemd-libs
  )
  optdepends=(
    'wireplumber-docs: Documentation'
  )
  provides=(pipewire-session-manager)
  conflicts=(pipewire-media-session)
  install=wireplumber.install

  meson install -C build --destdir "$pkgdir"

  (
    cd "$pkgdir"

    _pick libw usr/lib/libwireplumber-$_ver.so*
    _pick libw usr/lib/girepository-1.0
    _pick libw usr/lib/pkgconfig
    _pick libw usr/include
    _pick libw usr/share/gir-1.0

    _pick docs usr/share/doc
  )

  install -Dt "$pkgdir/usr/share/doc/$pkgname" -m644 $pkgbase/{NEWS,README}*
  install -Dt "$pkgdir/usr/share/licenses/$pkgname" -m644 $pkgbase/LICENSE
}

package_libwireplumber() {
  pkgdesc+=" - client library"
  depends=(
    gcc-libs
    glibc
    libg{lib,module,object,io}-2.0.so
    libpipewire-0.3.so
  )
  provides=(libwireplumber-$_ver.so)

  mv libw/* "$pkgdir"

  install -Dt "$pkgdir/usr/share/licenses/$pkgname" -m644 $pkgbase/LICENSE
}

# vim:set sw=2 et:
