# Maintainer: Simon Hallsten <flightlessmangoyt@gmail.com>
# Contributor: Emil Velikov <emil.l.velikov@gmail.com>

pkgname=('mangohud' 'lib32-mangohud')
pkgver=0.6.9.1.r16.g1093de8
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
  "mangohud"::"git+https://github.com/flightlessmango/MangoHud.git#commit=1093de8c4406a96642e139243911a571874c3d11"
  "imgui-v1.81.tar.gz::https://github.com/ocornut/imgui/archive/v1.81.tar.gz"
  "imgui-1.81-1-wrap.zip::https://wrapdb.mesonbuild.com/v1/projects/imgui/1.81/1/get_zip"
  "spdlog-1.8.5.tar.gz::https://github.com/gabime/spdlog/archive/v1.8.5.tar.gz"
  "spdlog-1.8.5-1-wrap.zip::https://wrapdb.mesonbuild.com/v1/projects/spdlog/1.8.5/1/get_zip"
  "nlohmann_json-3.10.5.zip::https://github.com/nlohmann/json/releases/download/v3.10.5/include.zip"
  "vulkan-headers-1.2.158.tar.gz::https://github.com/KhronosGroup/Vulkan-Headers/archive/v1.2.158.tar.gz"
  "vulkan-headers-1.2.158-2-wrap.zip::https://wrapdb.mesonbuild.com/v2/vulkan-headers_1.2.158-2/get_patch"
)

sha256sums=(
  'SKIP'
  'f7c619e03a06c0f25e8f47262dbc32d61fd033d2c91796812bf0f8c94fca78fb'
  '6d00b442690b6a5c5d8f898311daafbce16d370cf64f53294c3b8c5c661e435f'
  '944d0bd7c763ac721398dca2bb0f3b5ed16f67cef36810ede5061f35a543b4b8'
  '3c38f275d5792b1286391102594329e98b17737924b344f98312ab09929b74be'
  'b94997df68856753b72f0d7a3703b7d484d4745c567f3584ef97c96c25a5798e'
  '53361271cfe274df8782e1e47bdc9e61b7af432ba30acbfe31723f9df2c257f3'
  '860358cf5e73f458cd1e88f8c38116d123ab421d5ce2e4129ec38eaedd820e17'
)

pkgver() {
  cd mangohud
  git describe --tags | sed -r 's/^v//;s/([^-]*-g)/r\1/;s/-/./g'
}

prepare() {
  cd mangohud

  # meson subprojects
  ln -sv "$srcdir/imgui-1.81" subprojects
  ln -sv "$srcdir/spdlog-1.8.5" subprojects
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
