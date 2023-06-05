# Maintainer: Hans-Kristian Arntzen <post@arntzen-software.no>
# Contributor: Joshua Ashton <joshua@froggi.es>

# This package provides a minimal instance of RenderDoc
# that simply provides capturing and replay server facilities.
#
# If you need a GUI, grab that from renderdoc, as it provides qrenderdoc.

pkgname=renderdoc-minimal

# v1.27 + 2 commits which fix Deck memory issues on capture.
_commit=0f851df6c2f85c7f64b7cb680f53d0c57e21ae97

_minor_version=27
_pkgver=1.${_minor_version}
pkgver=1.27.r3.g0f851df
pkgrel=1

pkgdesc="OpenGL and Vulkan debugging tool (minimal, capture + replay server only)"
arch=(x86_64)
url="https://github.com/baldurk/renderdoc"
license=("MIT")
makedepends=("git" "cmake" "python")
depends=("libx11" "libxcb" "mesa" "libgl" "xcb-util-keysyms")
provides=("renderdoc")
conflicts=("renderdoc")
source=("renderdoc::git+https://github.com/baldurk/renderdoc.git#commit=${_commit}")
validpgpkeys=('1B039DB9A4718A2D699DE031AC612C3120C34695')
sha384sums=('SKIP')

pkgver() {
  cd renderdoc
  git describe --long --abbrev=7 | sed 's/\([^-]*-g\)/r\1/;s/-/./g' | sed 's/^v//'
}

prepare() {
  # Revert the bump to v1.28 server compatibility. This always comes right after a release,
  # but we want this package to be compatible with v1.27 stable UI clients.
  cd renderdoc
  sed -i renderdoc/api/replay/version.h -e "s/RENDERDOC_VERSION_MINOR .*$/RENDERDOC_VERSION_MINOR ${_minor_version}/"
}

build() {
  cmake -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DENABLE_QRENDERDOC=OFF \
        -DENABLE_PYRENDERDOC=OFF \
        -DBUILD_VERSION_STABLE=OFF \
        -DBUILD_VERSION_DIST_CONTACT="post@arntzen-software.no" \
        -DBUILD_VERSION_DIST_NAME="SteamOS" \
        -DBUILD_VERSION_DIST_VER="${pkgver}.steamos" \
        -B"${srcdir}/renderdoc"/build \
        -H"${srcdir}/renderdoc"
  cmake --build "${srcdir}/renderdoc"/build
}

package() {
  make DESTDIR="${pkgdir}" -C "${srcdir}/renderdoc"/build install
  mkdir -p "${pkgdir}/usr/share/licenses/${pkgname}"
  install -Dm644 "${srcdir}/renderdoc/LICENSE.md" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

# vim:set ts=2 sw=2 et:
