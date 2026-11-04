# Maintainer: Simon Hallsten <flightlessmangoyt@gmail.com>
# Contributor: Emil Velikov <emil.l.velikov@gmail.com>

pkgname=('mangohud' 'lib32-mangohud')
pkgver=0.8.4.r235.g8d76620f
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
  libxi
  libxnvctrl
  libxrandr
  'meson>=1.4.0'
  nlohmann-json
  python
  python-mako
  vulkan-icd-loader
  lib32-vulkan-icd-loader
)

depends=(libxkbcommon lib32-libxkbcommon)

source=(
  "mangohud"::"git+https://github.com/flightlessmango/MangoHud.git#commit=8d76620f71e92e5f686940404bfa7625a9034213"
  "imgui-1.91.6.tar.gz::https://github.com/ocornut/imgui/archive/refs/tags/v1.91.6.tar.gz"
  "imgui_1.91.6-3_patch.zip::https://wrapdb.mesonbuild.com/v2/imgui_1.91.6-3/get_patch"
  "spdlog-v1.14.1.tar.gz::https://github.com/gabime/spdlog/archive/refs/tags/v1.14.1.tar.gz"
  "spdlog-1.14.1-1-wrap.zip::https://wrapdb.mesonbuild.com/v2/spdlog_1.14.1-1/get_patch"
  "vulkan-headers-1.4.346.tar.gz::https://github.com/KhronosGroup/Vulkan-Headers/archive/v1.4.346.tar.gz"
  "vulkan-utility-libraries-1.4.346.tar.gz::https://github.com/KhronosGroup/Vulkan-Utility-Libraries/archive/v1.4.346.tar.gz"
  "implot-v0.16.zip::https://github.com/epezent/implot/archive/refs/tags/v0.16.zip"
  "implot-v0.16-1-wrap.zip::https://wrapdb.mesonbuild.com/v2/implot_0.16-1/get_patch"
)

sha256sums=('SKIP'
            'c5fbc5dcab1d46064001c3b84d7a88812985cde7e0e9ced03f5677bec1ba502a'
            '2f7977114ba07d06559aaf8890a92a4ebd25186592d4447954605aaf2244634d'
            '1586508029a7d0670dfcb2d97575dcdc242d3868a259742b69f100801ab4e16b'
            'ae878e732330ea1048f90d7e117c40c0cd2a6fb8ae5492c7955818ce3aaade6c'
            '5bb77f5d7b460e255a9e51affc00d64354986b55cf577d8eab28529cad01fc80'
            '372eb525103ecb4e3a04d030b2a9778ebc67853bbdc82ce6747de3757d432ad9'
            '24f772c688f6b8a6e19d7efc10e4923a04a915f13d487b08b83553aa62ae1708'
            '1c6b1462066a5452fa50c1da1dd47fed841f28232972c82d778f2962936568c7')

pkgver() {
  cd mangohud
  git describe --tags | sed -r 's/^v//;s/([^-]*-g)/r\1/;s/-/./g'
}

prepare() {
  cd mangohud

  local src
  for src in "${source[@]}"; do
    src="${src%%::*}"
    src="${src##*/}"
    [[ $src = *.patch ]] || continue
    echo "Applying patch $src..."
    patch -Np1 < "../$src"
  done

  # meson subprojects
  ln -sfnv "$srcdir/imgui-1.91.6" subprojects/imgui-1.91.6
  cp -rv subprojects/packagefiles/imgui-1.91.6/. subprojects/imgui-1.91.6/
  ln -sfv "$srcdir/implot-0.16" subprojects
  ln -sfnv "$srcdir/spdlog-1.14.1" subprojects/spdlog-1.14.1
  ln -sfnv "$srcdir/Vulkan-Headers-1.4.346" subprojects/Vulkan-Headers-1.4.346
  cp -rv subprojects/packagefiles/vulkan-headers/. subprojects/Vulkan-Headers-1.4.346/
  ln -sfnv "$srcdir/Vulkan-Utility-Libraries-1.4.346" subprojects/Vulkan-Utility-Libraries-1.4.346
  cp -rv subprojects/packagefiles/vulkan-utility-libraries/. subprojects/Vulkan-Utility-Libraries-1.4.346/
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
    -D with_mangohud_next=false
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
