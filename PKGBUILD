# Maintainer: Joshua Ashton <joshua@froggi.es>

# This package provides a minimal instance of RenderDoc
# that simply provides capturing and replay server facilities.
#
# If you need a GUI, grab that from renderdoc, as it provides qrenderdoc.

pkgname=renderdoc-minimal
pkgver=1.22
pkgrel=6
pkgdesc="OpenGL and Vulkan debugging tool (minimal, capture + replay server only)"
arch=(x86_64)
url="https://github.com/baldurk/renderdoc"
license=("MIT")
makedepends=("cmake" "python")
depends=("libx11" "libxcb" "mesa" "libgl" "xcb-util-keysyms")
provides=("renderdoc")
conflicts=("renderdoc")
source=("https://github.com/baldurk/renderdoc/archive/v${pkgver}.tar.gz"
        "https://github.com/baldurk/renderdoc/releases/download/v${pkgver}/v${pkgver}.tar.gz.asc")
validpgpkeys=('1B039DB9A4718A2D699DE031AC612C3120C34695')
sha384sums=('e94ff8a086420581106aefed4eac5f37ae3f4f207e819f6bf45f95bcfbf2488fabb7dee8e70913bf321bfc80ee2b3e03'
            'SKIP')

build() {
  cmake -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DENABLE_QRENDERDOC=OFF \
        -DENABLE_PYRENDERDOC=OFF \
        -DBUILD_VERSION_STABLE=ON \
        -DBUILD_VERSION_DIST_CONTACT="joshua@froggi.es" \
        -DBUILD_VERSION_DIST_NAME="SteamOS" \
        -DBUILD_VERSION_DIST_VER="${pkgver}" \
        -B"${srcdir}/renderdoc-${pkgver}"/build \
        -H"${srcdir}/renderdoc-${pkgver}"
  cmake --build "${srcdir}/renderdoc-${pkgver}"/build
}

package() {
  make DESTDIR="${pkgdir}" -C "${srcdir}/renderdoc-${pkgver}"/build install
  mkdir -p "${pkgdir}/usr/share/licenses/${pkgname}"
  install -Dm644 "${srcdir}/renderdoc-${pkgver}/LICENSE.md" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

# vim:set ts=2 sw=2 et: