# Maintainer: Simon Hallsten <flightlessmangoyt@gmail.com>
# Contributor: Emil Velikov <emil.l.velikov@gmail.com>

pkgname=('mangohud' 'lib32-mangohud')
pkgver=0.8.3.rc1.r18.g01b724d3
pkgrel=1
pkgdesc="Vulkan and OpenGL overlay to display performance information"
url="https://github.com/flightlessmango/MangoHud"
arch=(x86_64)
license=(MIT)
replaces=('vulkan-mesa-layer-mango')
makedepends=(
  dbus
  git
  glslang
  glew
  glfw-x11
  libglvnd
  lib32-libglvnd
  libx11
  libxnvctrl
  libxrandr
  meson
  python
  python-mako
)

depends=(libxkbcommon lib32-libxkbcommon)

source=(
  "mangohud"::"git+https://github.com/flightlessmango/MangoHud.git#commit=01b724d3e43f668babcbd70b550944bea4bdd524"
  "imgui-1.91.6.tar.gz::https://github.com/ocornut/imgui/archive/refs/tags/v1.91.6.tar.gz"
  "imgui_1.91.6-3_patch.zip::https://wrapdb.mesonbuild.com/v2/imgui_1.91.6-3/get_patch"
  "spdlog-v1.14.1.tar.gz::https://github.com/gabime/spdlog/archive/refs/tags/v1.14.1.tar.gz"
  "spdlog-1.14.1-1-wrap.zip::https://wrapdb.mesonbuild.com/v2/spdlog_1.14.1-1/get_patch"
  "vulkan-headers-1.3.283.tar.gz::https://github.com/KhronosGroup/Vulkan-Headers/archive/v1.3.283.tar.gz"
  "vulkan-headers-1.3.283-1-wrap.zip::https://wrapdb.mesonbuild.com/v2/vulkan-headers_1.3.283-1/get_patch"
  "implot-v0.16.zip::https://github.com/epezent/implot/archive/refs/tags/v0.16.zip"
  "implot-v0.16-1-wrap.zip::https://wrapdb.mesonbuild.com/v2/implot_0.16-1/get_patch"
)

sha256sums=('SKIP'
            'c5fbc5dcab1d46064001c3b84d7a88812985cde7e0e9ced03f5677bec1ba502a'
            '2f7977114ba07d06559aaf8890a92a4ebd25186592d4447954605aaf2244634d'
            '1586508029a7d0670dfcb2d97575dcdc242d3868a259742b69f100801ab4e16b'
            'ae878e732330ea1048f90d7e117c40c0cd2a6fb8ae5492c7955818ce3aaade6c'
            "a76ff77815012c76abc9811215c2167128a73a697bcc23948e858d1f7dd54a85"
            "00e30d35117ae90a19b5b8878746fceaf31b41778b817ca9e6b3ae6063be8233"
            '24f772c688f6b8a6e19d7efc10e4923a04a915f13d487b08b83553aa62ae1708'
            '1c6b1462066a5452fa50c1da1dd47fed841f28232972c82d778f2962936568c7')

pkgver() {
  cd mangohud
  git describe --tags | sed -r 's/^v//;s/([^-]*-g)/r\1/;s/-/./g'
}

prepare() {
  cd mangohud

  # meson subprojects
  ln -sv "$srcdir/imgui-1.91.6" subprojects
  ln -sv "$srcdir/spdlog-1.14.1" subprojects
  ln -sv "$srcdir/implot-0.16" subprojects
  ln -sv "$srcdir/Vulkan-Headers-1.3.283" subprojects
}

build() {
  local meson_options=(
    -D append_libdir_mangohud=false
  # Arch has only 64bit version
    -D use_system_spdlog=disabled
    -D mangoapp=false
    -D mangohudctl=false
    -D with_xnvctrl=disabled
  # Enable once mangohud can use system cmocka
    -D tests=disabled
  )

  arch-meson mangohud build64 "${meson_options[@]}" \
    -D mangoapp=true -D mangohudctl=true
  meson compile -C build64

  export CC="gcc -m32"
  export CXX="g++ -m32"
  export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"

  arch-meson mangohud build32 "${meson_options[@]}" --libdir=lib32
  meson compile -C build32
}

package_mangohud() {
  conflicts=('mangohud-common')
  depends=(
    glibc
    gcc-libs
  )
  # XXX: should really be optdepends
  depends+=(
    bash # for mangohud script
    dbus # media player info
    glew # for mangoapp
    glfw-x11 # for mangoapp
    libglvnd # for GL overlay
    libx11 # for mangoapp
  )

  meson install -C build64 --destdir "$pkgdir"
  install -m644 -Dt "$pkgdir/usr/share/licenses/$pkgname" mangohud/LICENSE
}

package_lib32-mangohud() {
  depends=(
    lib32-glibc
    lib32-gcc-libs
  )
  # XXX: should really be optdepends
  depends+=(
    lib32-dbus # media player info
    lib32-libglvnd # for GL overlay
  )

  meson install -C build32 --destdir "$pkgdir"
  install -m644 -Dt "$pkgdir/usr/share/licenses/$pkgname" mangohud/LICENSE

  rm -rf "$pkgdir/usr/bin"
  rm -rf "$pkgdir/usr/share/doc"
  rm -rf "$pkgdir/usr/share/icons"
  rm -rf "$pkgdir/usr/share/man"
  rm -rf "$pkgdir/usr/share/metainfo"
}
