# Maintainer: Hans-Kristian Arntzen <post@arntzen-software.no>
# Contributor: Joshua Ashton <joshua@froggi.es>

# This package provides a minimal instance of RenderDoc
# that simply provides capturing and replay server facilities.
#
# If you need a GUI, grab that from renderdoc, as it provides qrenderdoc.
#
# Holo: Use clang instead of GCC. RenderDoc is not really tested with GCC.
# Holo: Apply a small post-cmake hack to workaround Arch forcing LTCG for Qt. This breaks clang.
# Holo: Apply experimental wayland support which is required for Gamescope WSI layer to work,
# but should only apply to Deck. Should never be enabled by default in upstream PKGBUILD.

pkgname=renderdoc-minimal
pkgver=1.41
pkgrel=1.1
pkgdesc="OpenGL and Vulkan debugging tool (minimal, capture + replay server only)"
arch=(x86_64)
url="https://github.com/baldurk/renderdoc"
license=("MIT")
makedepends=("cmake" "python" "clang")
depends=("libx11" "libxcb" "mesa" "libgl" "xcb-util-keysyms")
provides=("renderdoc")
conflicts=("renderdoc")
source=("https://github.com/baldurk/renderdoc/archive/v${pkgver}.tar.gz"
        "https://github.com/baldurk/renderdoc/releases/download/v${pkgver}/v${pkgver}.tar.gz.asc"
        "renderdoc-export-symbols.patch")
validpgpkeys=('1B039DB9A4718A2D699DE031AC612C3120C34695')
sha384sums=('25bb82428fbabb105882d0653eaf0595e2e82ab7695a6dbba575692b75abf9fb9c5d1c6ae3c3a739725dd36e318ce7a2'
            'SKIP'
            '6870f290d2b9ddc5bd5ac599b226951c0f4bff101de7958b5d661d8d01e20a981385901c9ca2e89028fbc6d10fb6cfd5')

# Baldur recommends not using LTO.
options=(!lto)

prepare() {
  cd "${srcdir}/renderdoc-${pkgver}"

  # Fix marker symbol export
  patch -Np1 -i "${srcdir}/renderdoc-export-symbols.patch"
}

build() {
  # Baldur recommends clang over GCC.
  # For Gamescope WSI layer, we require Wayland to work,
  # so we have to enable the experimental feature despite its dubious nature.
  cmake -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DENABLE_QRENDERDOC=OFF \
        -DENABLE_PYRENDERDOC=OFF \
        -DBUILD_VERSION_STABLE=ON \
        -DCMAKE_C_COMPILER=clang \
        -DCMAKE_CXX_COMPILER=clang++ \
        -DENABLE_UNSUPPORTED_EXPERIMENTAL_POSSIBLY_BROKEN_WAYLAND=ON \
        -DBUILD_VERSION_DIST_CONTACT="post@arntzen-software.no" \
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
