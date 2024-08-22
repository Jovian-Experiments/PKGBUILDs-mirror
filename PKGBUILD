# Maintainer: Hans-Kristian Arntzen <post@arntzen-software.no>
# Contributor: Joshua Ashton <joshua@froggi.es>
#
# Based off the AUR package available here: https://aur.archlinux.org/packages/renderdoc
#
# Holo: Use clang instead of GCC. RenderDoc is not really tested with GCC.
# Holo: Apply a small post-cmake hack to workaround Arch forcing LTCG for Qt. This breaks clang.
# Holo: Apply experimental wayland support which is required for Gamescope WSI layer to work,
# but should only apply to Deck. Should never be enabled by default in upstream PKGBUILD.
# Holo: Back-port a patch from v1.x which fixes replay when using gamescope WSI layer.
# Only relevant for Deck.

pkgname=renderdoc
pkgver=1.34
pkgrel=1.1
pkgdesc="OpenGL and Vulkan debugging tool"
arch=(x86_64)
url="https://github.com/baldurk/renderdoc"
license=("MIT")
makedepends=("pcre" "cmake" "python" "clang")
depends=("libx11" "libxcb" "mesa" "libgl" "qt5-base" "qt5-svg" "qt5-x11extras" "xcb-util-keysyms")
source=("https://github.com/baldurk/renderdoc/archive/v${pkgver}.tar.gz"
        "https://github.com/baldurk/renderdoc/releases/download/v${pkgver}/v${pkgver}.tar.gz.asc"
        "0001-Strip-VK_EXT_hdr_metadata-extension-on-replay.patch")
validpgpkeys=('1B039DB9A4718A2D699DE031AC612C3120C34695')
sha384sums=('49502afa687d17cb8268fc25f90141837c406b7a2f001c2a9c5fb8c7c9e5d36e9e0bf2844bea4efa5a56adecc97b4303'
            'SKIP'
            'SKIP')

# Baldur recommends not using LTO.
options=(!lto)

prepare() {
  cd "${srcdir}/renderdoc-${pkgver}"
  # Backport from v1.x to deal with Gamescope WSI layer enabling HDR metadata while
  # plain replayer does not get WSI layer.
  patch -p1 < "../../0001-Strip-VK_EXT_hdr_metadata-extension-on-replay.patch"
}

build() {
  # Baldur recommends clang over GCC.
  # For Gamescope WSI layer, we require Wayland to work,
  # so we have to enable the experimental feature despite its dubious nature.
  cmake -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DBUILD_VERSION_STABLE=ON \
        -DCMAKE_C_COMPILER=clang \
        -DCMAKE_CXX_COMPILER=clang++ \
        -DENABLE_UNSUPPORTED_EXPERIMENTAL_POSSIBLY_BROKEN_WAYLAND=ON \
        -DBUILD_VERSION_DIST_CONTACT="post@arntzen-software.no" \
        -DBUILD_VERSION_DIST_NAME="SteamOS" \
        -DBUILD_VERSION_DIST_VER="${pkgver}" \
        -B"${srcdir}/${pkgname}-${pkgver}"/build \
        -H"${srcdir}/${pkgname}-${pkgver}"
  # For some reason, LTCG is enabled by default in qmake.
  # This seems to be an Arch Linux default for whatever reason, but it breaks renderdoc build.
  echo "CONFIG-=ltcg" >> "${srcdir}/${pkgname}-${pkgver}"/build/qrenderdoc/qrenderdoc_cmake.pri
  cmake --build "${srcdir}/renderdoc-${pkgver}"/build
}

package() {
  make DESTDIR="${pkgdir}" -C "${srcdir}/${pkgname}-${pkgver}"/build install
  mkdir -p "${pkgdir}/usr/share/licenses/$pkgname"
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}/LICENSE.md" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

# vim:set ts=2 sw=2 et:
