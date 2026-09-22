# Maintainer: David Runge <dvzrv@archlinux.org>
# Maintainer: Jan Alexander Steffens (heftig) <heftig@archlinux.org>
# Maintainer (Holo): Ludovico de Nittis <denittis@collabora.com>

pkgbase=wireplumber
pkgname=(
  wireplumber
  libwireplumber
  wireplumber-docs
)
pkgver=0.5.17
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
  glib2-devel
  glibc
  gobject-introspection
  graphviz
  libpipewire
  lua
  meson
  pipewire
  python-breathe
  python-lxml
  python-sphinx
  python-sphinx_rtd_theme
  systemd
  systemd-libs
)
checkdepends=(pipewire-audio)
source=(
  "git+https://gitlab.freedesktop.org/pipewire/$pkgbase.git#tag=$pkgver"

  # Holo: backport of https://gitlab.freedesktop.org/pipewire/wireplumber/-/merge_requests/667
  "0001-monitor-alsa-Add-node.create-loopback-property.patch"
  "0002-monitor-alsa-Don-t-make-the-loopback-device-node-vir.patch"
  "0003-monitor-alsa-Forward-the-session.suspend-timeout-sec.patch"
  "0004-monitor-alsa-Don-t-forward-priority.driver-property-.patch"
  "0005-monitor-alsa-Dont-set-node.dont-remix-property-to-lo.patch"
  "0006-monitor-alsa-Add-alsa.loopback-true-to-split-PCM-loo.patch"

  # Holo: Add ALSA setting to toggle external volume control. This cannot be merged upstream.
  # More info: https://gitlab.steamos.cloud/holo-team/tasks/-/work_items/2049
  "0001-alsa-Add-new-monitor.alsa.enable-external-volume-con.patch"
)
b2sums=('4a1366497e42c80178a4abc6d6e361e44226dd12898b82782e1e0a446a6b6e38589c12e76b1f046bd278f5ea453f5726799f44fbf310471cf554c8d89a39ba00'
        'ecb34e07d114e738521f7827a13be84982a5d670e53d6ae179ec0d997ea9342b75ca89e9862d34c83ebab5c9dd93bebceec2d6407d896d22a485b8107a3e9782'
        '9f0bd1cfe6e0470f08b43a3d2709d698ba8dc1899348b6d9770049a42acb933bc768b51fa3dafc902bc8d3a0ce42d8d2dbc3f68514dd14442b0de3baa436c035'
        '7cb72d359ab4f534baa93af86476ff31c5f5b1af9299e6ebf15bb42c89e981cc348235d3e813181356de2920186c878958b631296c99adf33d9e9ec459d120e5'
        'cfa50e2343f108e0314b0a1cdb2e73fcfe3d744b99b321e9ea90cc605920cde8c2d50c01883775c41e10bdeb0d2e2c17985e8918257a24864fb28aaa9cb675e5'
        'dcc9fdad8a9341ad1a475c7101a463b8b98cf6974c9c7816343621e416e587c0eebfbc44e6cdddf99f6758eb8f450986fa1a057c23c959a09f76044bdf5c1454'
        '3ce6f28aedef5603f05ebeb5360cbe71b7d714d9d82c68d680cebbd7e1e33ca898b4b1039959e877f38b6895be2aaaf9d769f1d3d9ea9054571086a80fdbc428'
        'b0189b00cc0b40a25f2c0bdf4b3d0d3764504137e770e867e4f3895f677e0ae2ebbe4c011ac0ca276c7f67dfbb1062d8a8c507fbf71850e0bf9c631308580616')

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
    pipewire
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

package_wireplumber-docs() {
  pkgdesc+=" - documentation"

  mv docs/* "$pkgdir"

  install -Dt "$pkgdir/usr/share/licenses/$pkgname" -m644 $pkgbase/LICENSE
}

# vim:set sw=2 sts=-1 et:
