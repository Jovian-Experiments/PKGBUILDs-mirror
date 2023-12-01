# Maintainer: Simon Hallsten <flightlessmangoyt@gmail.com>
# Contributor: Emil Velikov <emil.l.velikov@gmail.com>

pkgname=('mangohud' 'lib32-mangohud')
pkgver=josh.core.fix
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
  meson
  python-mako
)

source=(
  "mangohud"::"git+https://github.com/Joshua-Ashton/MangoHud.git#commit=f5da19168d7ef6c2226f15a98f4410225780bfd5"
  "imgui-v1.89.9.tar.gz::https://github.com/ocornut/imgui/archive/refs/tags/v1.89.9.tar.gz"
  "imgui-1.89-9-wrap.zip::https://wrapdb.mesonbuild.com/v2/imgui_1.89.9-1/get_patch"
  "spdlog-1.12.0.tar.gz::https://github.com/gabime/spdlog/archive/refs/tags/v1.12.0.tar.gz"
  "spdlog-1.12.0-1-wrap.zip::https://wrapdb.mesonbuild.com/v2/spdlog_1.12.0-1/get_patch"
  "nlohmann_json-3.10.5.zip::https://github.com/nlohmann/json/releases/download/v3.10.5/include.zip"
  "vulkan-headers-1.2.158.tar.gz::https://github.com/KhronosGroup/Vulkan-Headers/archive/v1.2.158.tar.gz"
  "vulkan-headers-1.2.158-2-wrap.zip::https://wrapdb.mesonbuild.com/v2/vulkan-headers_1.2.158-2/get_patch"
  "implot-v0.16.zip::https://github.com/epezent/implot/archive/refs/tags/v0.16.zip"
  "implot-v0.16-1-wrap.zip::https://wrapdb.mesonbuild.com/v2/implot_0.16-1/get_patch"
)

sha256sums=('SKIP'
            '1acc27a778b71d859878121a3f7b287cd81c29d720893d2b2bf74455bf9d52d6'
            '9b21290c597d76bf8d4eeb3f9ffa024b11d9ea6c61e91d648ccc90b42843d584'
            '4dccf2d10f410c1e2feaff89966bfc49a1abb29ef6f08246335b110e001e09a9'
            '0515906db7324df0e439bdd018bf019a60304430f6af8f1725910652e30ebe69'
            'b94997df68856753b72f0d7a3703b7d484d4745c567f3584ef97c96c25a5798e'
            '53361271cfe274df8782e1e47bdc9e61b7af432ba30acbfe31723f9df2c257f3'
            '860358cf5e73f458cd1e88f8c38116d123ab421d5ce2e4129ec38eaedd820e17'
            '24f772c688f6b8a6e19d7efc10e4923a04a915f13d487b08b83553aa62ae1708'
            '1c6b1462066a5452fa50c1da1dd47fed841f28232972c82d778f2962936568c7')

pkgver() {
  cd mangohud
  git describe --tags | sed -r 's/^v//;s/([^-]*-g)/r\1/;s/-/./g'
}

prepare() {
  cd mangohud

  # meson subprojects
  ln -sv "$srcdir/imgui-1.89.9" subprojects
  ln -sv "$srcdir/spdlog-1.12.0" subprojects
  ln -sv "$srcdir/implot-0.16" subprojects
  mkdir  subprojects/nlohmann_json-3.10.5
  ln -sv "$srcdir/include" subprojects/nlohmann_json-3.10.5/
  ln -sv "$srcdir/single_include" subprojects/nlohmann_json-3.10.5/
  ln -sv "$srcdir/LICENSE.MIT" subprojects/nlohmann_json-3.10.5/
  ln -sv "$srcdir/meson.build" subprojects/nlohmann_json-3.10.5/
  ln -sv "$srcdir/Vulkan-Headers-1.2.158" subprojects
}

build() {
  local meson_options=(
    -D append_libdir_mangohud=false
  # Arch has only 64bit version
    -D use_system_spdlog=disabled
    -D mangoapp=false
    -D mangoapp_layer=true
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
