import {
  useMutation,
  useQuery,
  useQueryClient,
} from "@tanstack/react-query";

import { salesService } from "../services/sales";

export function useSales(params = {}) {
  return useQuery({
    queryKey: ["sales", "list", params],
    queryFn: () => salesService.getSales(params),
  });
}

export function useSale(saleId, options = {}) {
  return useQuery({
    queryKey: ["sales", "detail", saleId],
    queryFn: () => salesService.getSale(saleId),
    enabled: Boolean(saleId),
    ...options,
  });
}

export function useCreateSale() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: (data) => salesService.createSale(data),
    onSuccess: () => {
      queryClient.invalidateQueries({
        queryKey: ["sales"],
      });
    },
  });
}

export function useUpdateSale() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: ({ saleId, data }) =>
      salesService.updateSale(saleId, data),
    onSuccess: (_, variables) => {
      queryClient.invalidateQueries({
        queryKey: ["sales"],
      });

      queryClient.invalidateQueries({
        queryKey: [
          "sales",
          "detail",
          variables.saleId,
        ],
      });
    },
  });
}

export function useDeleteSale() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: (saleId) =>
      salesService.deleteSale(saleId),
    onSuccess: () => {
      queryClient.invalidateQueries({
        queryKey: ["sales"],
      });
    },
  });
}

export function useUploadSales() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: (file) =>
      salesService.uploadSales(file),
    onSuccess: () => {
      queryClient.invalidateQueries({
        queryKey: ["sales"],
      });

      queryClient.invalidateQueries({
        queryKey: ["dashboard"],
      });
    },
  });
}