# Maintainer: David Runge <dvzrv@archlinux.org>
# Maintainer: Jan Alexander Steffens (heftig) <heftig@archlinux.org>
# Maintainer (Holo): Ludovico de Nittis <denittis@collabora.com>

pkgbase=wireplumber
pkgname=(
  wireplumber
  libwireplumber
)
pkgver=0.5.10
pkgrel=1.2
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
  # and https://gitlab.steamos.cloud/holo-team/tasks/-/issues/564
  "0001-access-default-Allow-defining-object-specific-permis.patch"
  "0002-monitor-alsa-Add-node.create-loopback-property.patch"
  "0003-monitor-alsa-Don-t-make-the-loopback-device-node-vir.patch"
  "0004-monitor-alsa-Dont-set-node-dont-remix-property.patch"

  # Holo: backport final patch of https://gitlab.freedesktop.org/pipewire/wireplumber/-/merge_requests/667/commits
  # Addresses https://gitlab.steamos.cloud/holo-team/tasks/-/issues/1340
  "0004-monitor-alsa-Forward-the-session.suspend-timeout-sec.patch"

  # Holo: backport of https://gitlab.freedesktop.org/pipewire/wireplumber/-/merge_requests/719 and
  # https://gitlab.freedesktop.org/pipewire/wireplumber/-/merge_requests/720
  # Fixes https://gitlab.steamos.cloud/holo-team/tasks/-/issues/1729
  "0001-monitor-alsa-increase-priority-for-usb-devices.patch"
  "0001-use-session-and-route-priorities.patch"

  # Holo: backport of https://gitlab.freedesktop.org/pipewire/wireplumber/-/merge_requests/721
  # Addresses https://gitlab.steamos.cloud/holo-team/tasks/-/issues/564
  "0001-create-item-Reconfigure-audio-adapters-if-node.featu.patch"
  "0002-m-si-audio-adapter-Add-new-item.features.mono-config.patch"
  "0003-config-Add-new-node.features.audio.mono-setting.patch"
)
b2sums=('5c9d06c4084187ce172e98fb05bef3826e4b7bf1fba505e5543fec0e194d8a957172c81e6fa32c7f53832e204dd794189d48deaae5eca10577b04106f2625ff3'
        '86f80f07bb5f446ae90f88f39870139d4d902f99048a62eb825ac12b654ca248568b17f8a1ca15777b41e0a11054345d023fc36a348372f15cb75b92a0180cfe'
        '09ab29570886efb01148edec25a0bb1bcc2ef20e7b02ed6f1fbaa0a29caa4b1f859717735b33fa93ca3494a36336c6730ed940f580ee78705d3c7b6fdc9d5735'
        '145fd614765ebe212de7e27e78b243bb294bd2fdc1efb1c6852280e8db2c2cbca40d6ce838013a06ced34bc030a16a11f1c4875562cd5d041c0785e7be712636'
        '46f72253266c5b9230678946d7b349a5726801d2dd038fa00748e0b5cf194b1d21812862399a95a11f2ae9942a2319304ba2cdd607f6fcacdf382ac5ca57aa01'
        '3b05b23dd3ff1da4f59df814780cf5251769c10ef3b1c07707ef717160631e27113e5e7286cd8b37ad4f37b21f9f14649d8fa5148b6aa90d26fef48a219e7e5e'
        'd8e0ff4f2c0927e1da127442c2c3d9aecaa05cca2753fdcb1786fe2ac6d959b0a995988e02f155de396fbe4fcb5eac3cbd55caa75be6d4a86eaa3e723415d062'
        'aba4d3fd93a4dafac5c1bb425621b176a80b3396f2896102c0c26399e86d9101165dabd0dee2c9d8964415e5098a8b78e87b564d2855de6c81f3eca489b183da'
        '0a6c56d194377a330a277463e614656e1c68618ed417834e8413c4897bb90d35404d1e4b85016b32ddecf20ccf42b0dd9eff4492e649a1d633b558ee9abe5b73'
        '42cc47d7f3119898f6560e85af44c812316c3babd8d439129054ef3c48782296c63f5f3f543a4b44700b197f0657c9d9bc863e8b03b02be01e24472e7c29f5a5'
        'c7381703ce9b75c0fd2a64676df6c3875b2baa319b1714fdced4578952010f37834322e6d836dacfc643659f8df1008e480f54bee881321736fe812a1bf70b97')

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
