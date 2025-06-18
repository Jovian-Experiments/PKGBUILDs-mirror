# Maintainer: David Runge <dvzrv@archlinux.org>
# Maintainer: Jan Alexander Steffens (heftig) <heftig@archlinux.org>
# Maintainer (Holo): Ludovico de Nittis <denittis@collabora.com>

pkgbase=wireplumber
pkgname=(
  wireplumber
  libwireplumber
)
pkgver=0.5.7
pkgrel=1.3
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
  'python>=3.13'
  'python<3.14'
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

  # Holo: backport of https://gitlab.freedesktop.org/pipewire/wireplumber/-/merge_requests/643
  # and https://gitlab.freedesktop.org/pipewire/wireplumber/-/merge_requests/667
  # Part of https://gitlab.steamos.cloud/holo-team/tasks/-/issues/1208
  "0001-access-default-Allow-defining-object-specific-permis.patch"
  "0002-monitor-alsa-Add-node.create-loopback-property.patch"
  "0003-monitor-alsa-Don-t-make-the-loopback-device-node-vir.patch"

  # Holo: backport of https://gitlab.freedesktop.org/pipewire/wireplumber/-/merge_requests/678
  # Part of https://gitlab.steamos.cloud/holo-team/tasks/-/issues/1208
  "0001-state-routes-only-save-route-properties-if-it-is-ava.patch"

  # Holo: backport of https://gitlab.freedesktop.org/pipewire/wireplumber/-/merge_requests/646
  # Part of https://gitlab.steamos.cloud/holo-team/tasks/-/issues/1173
  "0001-lib-Add-new-proc-utils-API-for-process-utilities.patch"
  "0002-scripts-Add-audio-group-utils.lua-to-group-audio-str.patch"

  # Holo: backport final patch of https://gitlab.freedesktop.org/pipewire/wireplumber/-/merge_requests/667/commits
  # Addresses https://gitlab.steamos.cloud/holo-team/tasks/-/issues/1340
  "0004-monitor-alsa-Forward-the-session.suspend-timeout-sec.patch"
)
b2sums=('4d57500277d7ba82a96996ead553b40bb7b0d5803cba1e8a1ac0ada25077dc10645e03a7aca32eba4e780311c67f2cdf2ddbc8dc147fd232823416867b682812'
        '86f80f07bb5f446ae90f88f39870139d4d902f99048a62eb825ac12b654ca248568b17f8a1ca15777b41e0a11054345d023fc36a348372f15cb75b92a0180cfe'
        'ea55591190916920756ee0cdab3d4d315500346370dc03a9b739bdcf9806aaec23cfafe31e35c89a6d53e3dd2d5001986012d29fcc77f3be1bf5eaa4ca486cb1'
        '145fd614765ebe212de7e27e78b243bb294bd2fdc1efb1c6852280e8db2c2cbca40d6ce838013a06ced34bc030a16a11f1c4875562cd5d041c0785e7be712636'
        '1498cd88ec907e93975e73af62e01fe0ab40d228603a433e502025b44322092bef0adb0dd508eb96a304c8bc94b00cabafd193ab2eb97d9aaaf699e441a133f3'
        'a93d7a763286ae7c243d3273bda656ddb3f978a285e26b395fa5ff53ec00fcd5cd138a97069af614d93105770bc45dc827c157676c931e5cdd43457548067150'
        'cda56c0e8f442fac5a7bb13cb915ebd28c21e62fd7ede3e3c84357ab20b5ff180c31e25c7064467d3d1237011ebd9d79745922b428681dbfefbae12580744937'
        '3b05b23dd3ff1da4f59df814780cf5251769c10ef3b1c07707ef717160631e27113e5e7286cd8b37ad4f37b21f9f14649d8fa5148b6aa90d26fef48a219e7e5e'
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

# vim:set sw=2 et:
