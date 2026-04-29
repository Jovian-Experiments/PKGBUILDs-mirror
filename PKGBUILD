# Maintainer: David Runge <dvzrv@archlinux.org>
# Maintainer: Jan Alexander Steffens (heftig) <heftig@archlinux.org>
# Maintainer (Holo): Ludovico de Nittis <denittis@collabora.com>

pkgbase=wireplumber
pkgname=(
  wireplumber
  libwireplumber
  wireplumber-docs
)
pkgver=0.5.14
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
  "0001-access-default-Allow-defining-object-specific-permis.patch"

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

  # Holo: backport of https://gitlab.freedesktop.org/pipewire/wireplumber/-/merge_requests/818
  "0001-properties-Add-API-to-clear-all-properties.patch"
  "0002-state-Add-new-WpStateMetadata-class.patch"
  "0003-m-lua-scripting-Add-Lua-API-for-new-WpStateMetadata-.patch"
  "0004-state-profile-Use-state-metadata-to-store-saved-prof.patch"

  # Holo: backport of https://gitlab.freedesktop.org/pipewire/wireplumber/-/merge_requests/819
  "0001-find-preferred-profile-Add-new-bluetooth.profile-pre.patch"
)
b2sums=('bdf2b17806b2ac30f4f40b4e1e35a9aecdf0660b24f75978e546e59d525bf4a97ad079a13d5b08d76d2d79d8b89f7093b777c5d92590ce2681490e3e114938e7'
        '6c1d7b3577d7836559ec5a896e275405764fc2fc0a7a9840e027e575bac47489e51b3c3f127e963335a8eb7d714068e0222c1dc05e8be38590e04205388113a8'
        '50cae746a48d2ec1700679bd7fe14227ab46fd0b26f829fedf7ef96f7bdd4edc6bac703c99acab586163f8c7d848c9465bcbc05a891a6a25422ff10b1b261140'
        '5a59c19d22c505e66c2aca7d888ab080be46fc2ac5d97090f9d01940a898dd4c42cd08868484ff4c4ef2006801f0385b803b1a4a9f922ce50fee43d5a5ab08da'
        'da1f9a77934203cb3f92f634e57aa5121e1e732a5f86e1068da955a0d07b663d64bef2c2868dde80c16ab24f5afc234267635a83ed2b64c61bf2913533762cd3'
        '5653ea6c4a01f275614f05c7ea3c52f2ad311a42fbad4b9780f4021609574327a96e9e91df493bc13593ac35daa0e77be2f1a672b7d12eaceb4cca0e3790e32a'
        'bc2633425fb1ff3aec54b09a1ef8ab9714b482c014ba7fd4af234196dbd9aa038101c84f862583331bb15c572bd95cc21cf83650c09963c13d22c3cbfbe62fd0'
        'daf1300f45171a549112fc1f2f8800ea14a51ce97159cbcac405beee469114697ce5ff296126be33fbf9bc76eae1f12a2798d65dbc4ec5bbe07fd6a5f081c318'
        '1d74a32c602d233d41961507802a59ec95da2d3945208d4643a75af7df0cb341bed91e6a4fa6306d5c64101cbd03525611e67d8349d17f2d0cb2719bc507bad0'
        '8b41df3a8b1309134868ef0ef421537da2e26661af3a92ed5aae8007b26c93abe1d2d351a8006ecc70d9fa5c8e43d7f34b2b679c6fc784808103c8ad1077ce53'
        '484cbbe10f24f001833ac276eb1fbbf64af4676006f566e6f2634ce0c48c13e44dc98182d034d15bb5ffcafdcf2f38881201f730d19231187dc5f1c0c4df1a1c'
        'f845596209389f6cc5fc7a73238e0f4e559c69d3fe216c93f25e5170ace558f2169f4c15de29bbb05aad222b1d9e83e7d799112feb2439864dc9a833f1373cad'
        '1069051c36c8e8c0470ff65560d9085317f32854661d68a8e4e137a6c0b51b66855358302fbb7d77a71016f1cae77703ba7295bc4ef5cfa6234f2a93dd4a7528'
        'a4fe84e7aa1bf13f467af6fca0469e280693b00632c3de5d985139b1e8b1b4b450016e4a8579ce26ea7c0fae4f1629cceaad86beab02a9fa78e4f53ac2660b74')

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
