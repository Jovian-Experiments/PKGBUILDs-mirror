# Maintainer: Simon Hallsten <flightlessmangoyt@gmail.com>
pkgname=('mangohud' 'lib32-mangohud')
pkgver=0.6.8.r139.gce5e068
pkgrel=1
pkgdesc="Vulkan and OpenGL overlay to display performance information"
arch=('x86_64')
makedepends=('dbus' 'gcc' 'meson' 'python-mako' 'libx11' 'lib32-libx11' 'git' 'pkgconf' 'vulkan-headers' 'appstream')
depends=('glslang' 'libglvnd' 'lib32-libglvnd' 'glew' 'glfw-x11')
replaces=('vulkan-mesa-layer-mango')
license=('MIT')
source=("mangohud"::"git+https://github.com/flightlessmango/MangoHud.git#commit=ce5e0683f0904f78e3666cdd0014d8ae1d915239"
        "mangohud-minhook"::"git+https://github.com/flightlessmango/minhook.git"
        "imgui-v1.81.tar.gz::https://github.com/ocornut/imgui/archive/v1.81.tar.gz"
        "imgui-1.81-1-wrap.zip::https://wrapdb.mesonbuild.com/v1/projects/imgui/1.81/1/get_zip"
        "spdlog-1.8.5.tar.gz::https://github.com/gabime/spdlog/archive/v1.8.5.tar.gz"
        "spdlog-1.8.5-1-wrap.zip::https://wrapdb.mesonbuild.com/v1/projects/spdlog/1.8.5/1/get_zip"
        "nlohmann_json-3.10.5.zip::https://github.com/nlohmann/json/releases/download/v3.10.5/include.zip"
        "vulkan-headers-1.2.158.tar.gz::https://github.com/KhronosGroup/Vulkan-Headers/archive/v1.2.158.tar.gz"
        "vulkan-headers-1.2.158-2-wrap.zip::https://wrapdb.mesonbuild.com/v2/vulkan-headers_1.2.158-2/get_patch"
        "cmocka-1.1.5.tar.xz::https://cmocka.org/files/1.1/cmocka-1.1.5.tar.xz"
        "cmocka_1.1.5-5_patch.zip::https://wrapdb.mesonbuild.com/v2/cmocka_1.1.5-5/get_patch"
        "mangohud.presets")

sha256sums=('SKIP'
            'SKIP'
            'f7c619e03a06c0f25e8f47262dbc32d61fd033d2c91796812bf0f8c94fca78fb'
            '6d00b442690b6a5c5d8f898311daafbce16d370cf64f53294c3b8c5c661e435f'
            '944d0bd7c763ac721398dca2bb0f3b5ed16f67cef36810ede5061f35a543b4b8'
            '3c38f275d5792b1286391102594329e98b17737924b344f98312ab09929b74be'
            'b94997df68856753b72f0d7a3703b7d484d4745c567f3584ef97c96c25a5798e'
            "53361271cfe274df8782e1e47bdc9e61b7af432ba30acbfe31723f9df2c257f3"
            "860358cf5e73f458cd1e88f8c38116d123ab421d5ce2e4129ec38eaedd820e17"
            'f0ccd8242d55e2fd74b16ba518359151f6f8383ff8aef4976e48393f77bba8b6'
            'e380083690849bb1abf231c42c684ec39a2dd1180c42d348b672ae6924b188d0'
            '6c7a1a21bf553d29eb88e765ab4a945ea7189bf3219ff604314a1cc1c8f31a13')

_build_args="-Dappend_libdir_mangohud=false -Dwith_xnvctrl=disabled -Dmangoapp_layer=true"

pkgver() {
  cd "$srcdir/mangohud"
  git describe --tags | sed -r 's/^v//;s/([^-]*-g)/r\1/;s/-/./g'
}

prepare() {
  cd "${srcdir}/mangohud"
  git submodule init
  git config submodule.modules/minhook.url "$srcdir/mangohud-minhook"
  git -c protocol.file.allow=always submodule update

  # meson subprojects
  ln -sv "$srcdir/imgui-1.81" subprojects
  ln -sv "$srcdir/spdlog-1.8.5" subprojects
  mkdir  subprojects/nlohmann_json-3.10.5
  ln -sv "$srcdir/include" subprojects/nlohmann_json-3.10.5/
  ln -sv "$srcdir/single_include" subprojects/nlohmann_json-3.10.5/
  ln -sv "$srcdir/LICENSE.MIT" subprojects/nlohmann_json-3.10.5/
  ln -sv "$srcdir/meson.build" subprojects/nlohmann_json-3.10.5/
  ln -sv "$srcdir/Vulkan-Headers-1.2.158" subprojects
  ln -sv "$srcdir/cmocka-1.1.5" subprojects
}

build() {
  arch-meson mangohud build64 \
    -D tests=disabled \
    ${_build_args} -Dmangoapp=true -Dmangohudctl=true

  ninja -C build64
  export CC="gcc -m32"
  export CXX="g++ -m32"
  export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/lib/i386-linux-gnu/pkgconfig:/usr/lib/pkgconfig:${PKG_CONFIG_PATH_32}"

  arch-meson mangohud build32 \
    -D tests=disabled \
    --libdir=lib32 \
    ${_build_args}

  ninja -C build32
}

package_mangohud() {
  provides=("mangohud")
  conflicts=('mangohud-common')
  DESTDIR="${pkgdir}" ninja -C build64 install
  mkdir -p $pkgdir/etc/MangoHud
  cp $srcdir/mangohud.presets $pkgdir/etc/MangoHud
}

package_lib32-mangohud() {
  provides=("lib32-mangohud")
  DESTDIR="${pkgdir}" ninja -C build32 install
  rm -rf "$pkgdir/usr/bin"
  rm -rf "$pkgdir/usr/share"
}
