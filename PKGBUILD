# Maintainer: David Runge <dvzrv@archlinux.org>
# Maintainer: Jan Alexander Steffens (heftig) <heftig@archlinux.org>
# Maintainer (Holo): Ludovico de Nittis <denittis@collabora.com>

pkgbase=wireplumber
pkgname=(
  wireplumber
  libwireplumber
)
pkgver=0.5.13
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
  "0001-access-default-Allow-defining-object-specific-permis.patch"

  # Holo: backport of https://gitlab.freedesktop.org/pipewire/wireplumber/-/merge_requests/667
  "0001-monitor-alsa-Add-node.create-loopback-property.patch"
  "0002-monitor-alsa-Don-t-make-the-loopback-device-node-vir.patch"
  "0003-monitor-alsa-Forward-the-session.suspend-timeout-sec.patch"
  "0004-monitor-alsa-Don-t-forward-priority.driver-property-.patch"
  "0005-monitor-alsa-Dont-set-node.dont-remix-property-to-lo.patch"
  "0006-monitor-alsa-Add-alsa.loopback-true-to-split-PCM-loo.patch"

  # Holo: backport of https://gitlab.freedesktop.org/pipewire/wireplumber/-/merge_requests/772
  "0001-apply-routes.lua-Add-a-mechanism-for-per-device-defa.patch"

  # Holo: backport of https://gitlab.freedesktop.org/pipewire/wireplumber/-/merge_requests/777
  "0001-autoswitch-bluetooth-profile-Fix-attempt-to-index-a-.patch"

  # Holo: backport of https://gitlab.freedesktop.org/pipewire/wireplumber/-/merge_requests/778
  "0001-monitors-bluez-Avoid-recreating-A2DP-SCO-nodes-if-lo.patch"
)
b2sums=('3b4b3c1b8fd00ff7ed149fa893c4d467a2605d3eb5ef8c8c3e265bd20438db58464d5ede4f8deabb48f2200fca5616d8511e022c0c6497062b15cbdbae97c83e'
        '6c1d7b3577d7836559ec5a896e275405764fc2fc0a7a9840e027e575bac47489e51b3c3f127e963335a8eb7d714068e0222c1dc05e8be38590e04205388113a8'
        '50cae746a48d2ec1700679bd7fe14227ab46fd0b26f829fedf7ef96f7bdd4edc6bac703c99acab586163f8c7d848c9465bcbc05a891a6a25422ff10b1b261140'
        '5a59c19d22c505e66c2aca7d888ab080be46fc2ac5d97090f9d01940a898dd4c42cd08868484ff4c4ef2006801f0385b803b1a4a9f922ce50fee43d5a5ab08da'
        'da1f9a77934203cb3f92f634e57aa5121e1e732a5f86e1068da955a0d07b663d64bef2c2868dde80c16ab24f5afc234267635a83ed2b64c61bf2913533762cd3'
        '5653ea6c4a01f275614f05c7ea3c52f2ad311a42fbad4b9780f4021609574327a96e9e91df493bc13593ac35daa0e77be2f1a672b7d12eaceb4cca0e3790e32a'
        'bc2633425fb1ff3aec54b09a1ef8ab9714b482c014ba7fd4af234196dbd9aa038101c84f862583331bb15c572bd95cc21cf83650c09963c13d22c3cbfbe62fd0'
        'daf1300f45171a549112fc1f2f8800ea14a51ce97159cbcac405beee469114697ce5ff296126be33fbf9bc76eae1f12a2798d65dbc4ec5bbe07fd6a5f081c318'
        '150c5880134409c61fab594d9c5bee38302b9e043ccd57b4c0268d8607b6bfb75b4ca5df2fae146ed13d7447c6b175529cede1bc7032c69440e885692b0d4cef'
        '5af57d070641d83059c1a929a164d653acc17cd66da666cac6206d3961b2f6a17069b0028cad8b7f031bb7583427cb7385b93ff084c882cd359879f4add089e8'
        'c4a7215ae1d1ceeb2daa55e29435a7e231400f1cc24a0b727784710dbda250f31b6c5141fc7bcb95e1406bbdce8893d38390a03eabc4609dd6dd740d84e13400')

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

# vim:set sw=2 sts=-1 et:
